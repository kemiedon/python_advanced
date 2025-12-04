"""example_json_sys.py

示範 json 與 sys 的簡單用法
"""

import sys
import json


def demo():
    print("sys.argv =", sys.argv)
    data = {"name": "Amy", "age": 20}
    s = json.dumps(data, ensure_ascii=False)
    print("json =", s)
    print("loads =", json.loads(s))


if __name__ == "__main__":
    demo()
