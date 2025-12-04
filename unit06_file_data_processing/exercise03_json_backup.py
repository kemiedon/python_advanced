"""exercise03_json_backup.py

練習 3：JSON 資料備份與還原（難度：⭐⭐）

任務：
1. 建立一個函式 create_student_data()，產生學生資料（Python 字典清單）
2. 建立一個函式 backup_to_json(data, filename)，將資料備份為 JSON 檔案
3. 建立一個函式 restore_from_json(filename)，從 JSON 檔案還原資料
4. 建立一個函式 search_student(data, name)，搜尋指定學生的資料
5. 測試備份、還原與搜尋功能
"""

import json


def create_student_data():
    """產生學生資料"""
    students = [
        {
            "id": "S001",
            "name": "小明",
            "age": 20,
            "grades": {"國文": 85, "英文": 90, "數學": 88},
            "hobbies": ["閱讀", "運動"],
        },
        {
            "id": "S002",
            "name": "小美",
            "age": 19,
            "grades": {"國文": 92, "英文": 87, "數學": 95},
            "hobbies": ["音樂", "繪畫"],
        },
        {
            "id": "S003",
            "name": "阿強",
            "age": 21,
            "grades": {"國文": 78, "英文": 82, "數學": 80},
            "hobbies": ["運動", "電玩"],
        },
        {
            "id": "S004",
            "name": "阿花",
            "age": 20,
            "grades": {"國文": 88, "英文": 91, "數學": 86},
            "hobbies": ["閱讀", "旅行"],
        },
    ]

    print("✓ 學生資料已建立")
    return students


def backup_to_json(data, filename):
    """將資料備份為 JSON 檔案"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✓ 資料已備份到：{filename}")
        return True
    except Exception as e:
        print(f"✗ 備份失敗：{e}")
        return False


def restore_from_json(filename):
    """從 JSON 檔案還原資料"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"✓ 資料已從 {filename} 還原")
        print(f"  共還原 {len(data)} 筆學生資料")
        return data
    except FileNotFoundError:
        print(f"✗ 找不到檔案：{filename}")
        return None
    except json.JSONDecodeError:
        print(f"✗ JSON 格式錯誤")
        return None
    except Exception as e:
        print(f"✗ 還原失敗：{e}")
        return None


def search_student(data, name):
    """搜尋指定學生的資料"""
    print(f"\n=== 搜尋學生：{name} ===")

    for student in data:
        if student["name"] == name:
            print(f"找到學生：")
            print(f"  學號：{student['id']}")
            print(f"  姓名：{student['name']}")
            print(f"  年齡：{student['age']}")
            print(f"  成績：{student['grades']}")
            print(f"  興趣：{', '.join(student['hobbies'])}")

            # 計算平均分數
            grades = student["grades"]
            avg = sum(grades.values()) / len(grades)
            print(f"  平均：{avg:.2f}")

            return student

    print(f"✗ 找不到學生：{name}")
    return None


def add_student(data, student_info):
    """新增學生資料"""
    data.append(student_info)
    print(f"✓ 已新增學生：{student_info['name']}")


def display_all_students(data):
    """顯示所有學生資料"""
    print(f"\n=== 所有學生資料 ===")

    for student in data:
        grades = student["grades"]
        avg = sum(grades.values()) / len(grades)
        print(
            f"{student['id']} {student['name']} （{student['age']} 歲）- 平均：{avg:.2f}"
        )


if __name__ == "__main__":
    # 1. 建立學生資料
    students = create_student_data()

    # 2. 顯示所有學生
    display_all_students(students)

    # 3. 備份到 JSON
    backup_to_json(students, "students_backup.json")

    # 4. 模擬清空資料
    print("\n--- 模擬資料遺失 ---")
    students = None

    # 5. 從 JSON 還原
    print("\n--- 還原資料 ---")
    students = restore_from_json("students_backup.json")

    # 6. 搜尋學生
    if students:
        search_student(students, "小美")
        search_student(students, "不存在的學生")

    # 7. 新增學生並重新備份
    print("\n--- 新增學生 ---")
    new_student = {
        "id": "S005",
        "name": "小華",
        "age": 19,
        "grades": {"國文": 90, "英文": 88, "數學": 92},
        "hobbies": ["攝影", "音樂"],
    }
    add_student(students, new_student)

    # 8. 更新備份
    backup_to_json(students, "students_backup.json")

    # 9. 再次顯示所有學生
    display_all_students(students)

    print("\n=== 完成 ===")
