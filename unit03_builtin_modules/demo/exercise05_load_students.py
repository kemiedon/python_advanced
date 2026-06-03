"""load_students.py

讀取 students.json 並列印內容
用法：python3 load_students.py students.json
"""
import json
from pathlib import Path

# 建立學生json檔
students = [{"name": "小明", "student_no": "ISP0001", "class": "6年1班" }, 
            {"name": "大雄", "student_no": "ISP0055", "class": "6年5班" },
            {"name": "小花", "student_no": "ISP0012", "class": "6年3班" }]

# 使用 Path(__file__).parent 取得目前這份 .py 檔所在的目錄
# folder = "\my_practice\\0603"
# current_dir = os.getcwd() + folder
current_dir = Path(__file__).parent

filename = "students3.json"
full_path = current_dir / filename

print(f"完整路徑:{full_path}")

students.append({"name": "胖虎", "student_no": "ISP0025", "class": "6年5班" })
with open(full_path, "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)

print(f"學生資料已存到: {full_path}")

print("=" * 70)
print("=====載入學生資料到list new_students的變數中========")
def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
if __name__ == "__main__":
    new_students = load_data(full_path)
    print(f"學生資料: {new_students}")