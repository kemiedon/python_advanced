"""exercise04_filesystem.py

練習 4：檔案系統基本操作
"""

import os
from pathlib import Path


def list_files(path):
    p = Path(path)
    return [x.name for x in p.iterdir() if x.is_file()]


def ensure_dir(path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def group_by_extension(path):
    files = list_files(path)
    groups = {}
    for f in files:
        ext = Path(f).suffix.lower()
        groups.setdefault(ext, []).append(f)
    return groups


if __name__ == "__main__":
    d = ensure_dir("unit04_testdir")
    print("list_files:", list_files("."))
    print("group_by_extension:", group_by_extension("."))
