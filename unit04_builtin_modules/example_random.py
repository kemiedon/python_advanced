"""example_random.py

示範 random 模組
"""

import random


def demo():
    students = ["小明", "小美", "阿強", "阿花", "Amy", "John"]
    print("students =", students)
    print("choice =", random.choice(students))
    print("sample(3) =", random.sample(students, 3))
    random.shuffle(students)
    print("shuffled =", students)


if __name__ == "__main__":
    demo()
