#!/usr/bin/env python3
"""
自動 push 腳本
- 自動 commit 所有 changes
- commit message 使用 a, b, c... z, aa, ab, ac... ba, bb, bc... 的規則
- 檢查前一個 commit 是否遵循規範，如果沒有則從 a 開始
- 自動處理子模組的 push
"""

import subprocess
import re
import sys
import time
import os


DEFAULT_ENCODING = 'utf-8'
WAIT_TIME = 1  # 等待檔案寫入的時間（秒）


def run_git(args, check=True):
    """統一執行 git，避免 Windows 預設編碼造成解碼失敗。"""
    return subprocess.run(
        ['git', *args],
        capture_output=True,
        text=True,
        encoding=DEFAULT_ENCODING,
        errors='replace',
        check=check,
    )


def get_previous_commit_message():
    """取得前一個 commit message"""
    try:
        result = run_git(['log', '-1', '--pretty=%B'], check=True)
        return (result.stdout or '').strip()
    except subprocess.CalledProcessError:
        return None


def is_valid_message(message):
    """檢查 message 是否符合規範 (a-z, aa-zz, aaa-zzz...)"""
    return bool(re.match(r'^[a-z]+$', message))


def generate_next_message(current_message):
    """根據當前 message 生成下一個 message"""
    if not current_message or not is_valid_message(current_message):
        return 'a'

    # 轉換為數字系統 (a=0, b=1, ..., z=25)
    # a, b, c, ..., z (26個)
    # aa, ab, ac, ..., az, ba, bb, ..., zz (676個)
    # 以此類推

    def message_to_number(msg):
        """將 message 轉換為數字"""
        num = 0
        for char in msg:
            num = num * 26 + (ord(char) - ord('a') + 1)
        return num

    def number_to_message(num):
        """將數字轉換回 message"""
        if num <= 0:
            return 'a'

        result = []
        while num > 0:
            num -= 1
            result.append(chr(ord('a') + (num % 26)))
            num //= 26

        return ''.join(reversed(result))

    current_num = message_to_number(current_message)
    next_num = current_num + 1
    return number_to_message(next_num)


def run_command(command, description):
    """執行命令並顯示狀態"""
    try:
        print(f"執行: {description}...")
        if command and command[0] == 'git':
            result = run_git(command[1:], check=True)
        else:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding=DEFAULT_ENCODING,
                errors='replace',
                check=True,
            )
        print(f"✓ {description} 完成")
        return True
    except subprocess.CalledProcessError as e:
        stderr = (e.stderr or '').strip()
        print(f"✗ {description} 失敗: {stderr}")
        return False


def process_submodule(submodule_path):
    """處理單個 submodule 的 commit 和 push"""
    original_dir = os.getcwd()

    try:
        # 確保路徑存在
        if not os.path.exists(submodule_path):
            print(f"✗ Submodule {submodule_path} 不存在")
            return False

        os.chdir(submodule_path)

        # 等待檔案寫入
        time.sleep(WAIT_TIME)

        # 檢查是否有變更
        result = run_git(['status', '--porcelain'], check=False)
        if not result.stdout.strip():
            return True

        # 取得前一個 commit message
        prev_message = get_previous_commit_message()
        next_message = generate_next_message(prev_message)

        print(f"\n[Submodule: {submodule_path}]")
        print(f"前一個 commit: {prev_message if prev_message else '無'}")
        print(f"下一個 commit: {next_message}")

        # Add, commit, push
        if not run_command(['git', 'add', '-A'], "git add -A"):
            return False
        if not run_command(['git', 'commit', '-m', next_message], f"git commit -m '{next_message}'"):
            return False
        if not run_command(['git', 'push'], "git push"):
            return False

        print(f"✓ Submodule {submodule_path} 完成")
        return True

    except Exception as e:
        print(f"✗ Submodule {submodule_path} 錯誤: {e}")
        return False
    finally:
        os.chdir(original_dir)


def main():
    print("=== 自動 Push 腳本 ===\n")

    # 檢查 git 倉庫
    try:
        run_git(['rev-parse', '--git-dir'], check=True)
    except subprocess.CalledProcessError:
        print("錯誤: 不是 git 倉庫")
        sys.exit(1)

    # 等待檔案寫入
    print("等待檔案寫入...")
    time.sleep(WAIT_TIME)

    # 處理所有 submodules
    print("檢查 submodules...")
    result = run_git(['config', '--file', '.gitmodules', '--name-only', '--get-regexp', 'path'], check=False)
    if result.stdout.strip():
        print("發現 submodules，先進行提交...\n")
        for line in result.stdout.strip().split('\n'):
            if not line.strip():
                continue
            # 格式: submodule.<name>.path
            try:
                # 從 git config 取得實際的 submodule 路徑
                path_result = run_git(['config', '--file', '.gitmodules', '--get', line], check=False)
                if path_result.stdout.strip():
                    submodule_path = path_result.stdout.strip()
                    process_submodule(submodule_path)
            except Exception as e:
                print(f"提取 submodule 路徑失敗: {e}")

    # 檢查主倉庫是否有 changes (包含 submodule reference 更新)
    print("\n檢查主倉庫變更...")
    result = run_git(['status', '--porcelain'], check=False)
    if not result.stdout.strip():
        print("無任何 changes，無須 commit")
        return

    # 取得前一個 commit message
    prev_message = get_previous_commit_message()
    print(f"[主倉庫]")
    print(f"前一個 commit message: {prev_message if prev_message else '無'}")

    # 生成下一個 message
    next_message = generate_next_message(prev_message)
    print(f"下一個 commit message: {next_message}\n")

    # git add all
    if not run_command(['git', 'add', '-A'], "git add -A"):
        sys.exit(1)

    # git commit
    if not run_command(['git', 'commit', '-m', next_message], f"git commit -m '{next_message}'"):
        sys.exit(1)

    # git push
    if not run_command(['git', 'push'], "git push"):
        sys.exit(1)

    print("\n✓ 所有操作完成")


if __name__ == '__main__':
    main()
