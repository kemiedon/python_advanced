"""example03_json_operations.py

示範 JSON 序列化與反序列化
"""

import json


def demo_json_dumps():
    """示範將 Python 資料轉成 JSON 字串"""
    print("=== 示範 JSON 序列化（dumps）===")

    # Python 字典
    student = {
        "name": "小明",
        "age": 20,
        "grades": {"國文": 85, "英文": 90, "數學": 88},
        "hobbies": ["閱讀", "運動", "音樂"],
    }

    # 轉成 JSON 字串
    json_str = json.dumps(student, ensure_ascii=False, indent=2)
    print("Python 物件：")
    print(student)
    print("\nJSON 字串：")
    print(json_str)
    print(f"\n資料型態：{type(json_str)}")


def demo_json_loads():
    """示範將 JSON 字串轉回 Python 資料"""
    print("\n=== 示範 JSON 反序列化（loads）===")

    json_str = '{"name": "小美", "age": 19, "grades": {"國文": 92, "英文": 87}}'

    # 轉回 Python 物件
    student = json.loads(json_str)
    print("JSON 字串：")
    print(json_str)
    print("\nPython 物件：")
    print(student)
    print(f"資料型態：{type(student)}")
    print(f"姓名：{student['name']}")
    print(f"國文成績：{student['grades']['國文']}")


def demo_json_dump_file():
    """示範將資料寫入 JSON 檔案"""
    print("\n=== 寫入 JSON 檔案 ===")

    students = [
        {"name": "小明", "age": 20, "grades": {"國文": 85, "英文": 90, "數學": 88}},
        {"name": "小美", "age": 19, "grades": {"國文": 92, "英文": 87, "數學": 95}},
        {"name": "阿強", "age": 21, "grades": {"國文": 78, "英文": 82, "數學": 80}},
    ]

    # 寫入檔案
    with open("students_backup.json", "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

    print("✓ 已寫入 JSON 檔案：students_backup.json")


def demo_json_load_file():
    """示範從 JSON 檔案讀取資料"""
    print("\n=== 從 JSON 檔案讀取 ===")

    with open("students_backup.json", "r", encoding="utf-8") as f:
        students = json.load(f)

    print("讀取到的學生資料：")
    for student in students:
        print(f"- {student['name']}，{student['age']} 歲")
        print(f"  成績：{student['grades']}")


def demo_nested_json():
    """示範複雜的巢狀 JSON 結構"""
    print("\n=== 複雜巢狀結構 ===")

    school_data = {
        "school_name": "資展高中",
        "classes": [
            {
                "class_name": "一年一班",
                "teacher": "王老師",
                "students": [
                    {"name": "小明", "score": 85},
                    {"name": "小美", "score": 92},
                ],
            },
            {
                "class_name": "一年二班",
                "teacher": "李老師",
                "students": [
                    {"name": "阿強", "score": 78},
                    {"name": "阿花", "score": 88},
                ],
            },
        ],
    }

    # 寫入檔案
    with open("school_data.json", "w", encoding="utf-8") as f:
        json.dump(school_data, f, ensure_ascii=False, indent=2)

    print("✓ 已寫入複雜結構：school_data.json")

    # 讀取並展示
    with open("school_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"\n學校名稱：{data['school_name']}")
    for class_info in data["classes"]:
        print(f"\n班級：{class_info['class_name']} （導師：{class_info['teacher']}）")
        for student in class_info["students"]:
            print(f"  - {student['name']}：{student['score']} 分")


if __name__ == "__main__":
    demo_json_dumps()
    demo_json_loads()
    demo_json_dump_file()
    demo_json_load_file()
    demo_nested_json()

    print("\n=== 完成 ===")
