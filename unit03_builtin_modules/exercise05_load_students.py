"""load_students.py

讀取 students.json 並列印內容
用法：python3 load_students.py students.json
"""

import sys
import json


def load_students(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python load_students.py students.json")
    else:
        filename = sys.argv[1]
        data = load_students(filename)
        print("Loaded:", data)
