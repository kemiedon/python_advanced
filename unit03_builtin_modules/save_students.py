"""save_students.py

示範：使用 sys.argv 與 json 將學生清單存檔
用法：python3 save_students.py students.json
"""

import sys
import json


def save_students(filename, students):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python save_students.py students.json")
    else:
        filename = sys.argv[1]
        students = [
            {"name": "小明", "score": 85},
            {"name": "小美", "score": 90},
        ]
        save_students(filename, students)
        print("Saved", filename)
