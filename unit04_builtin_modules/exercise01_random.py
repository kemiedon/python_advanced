"""exercise01_random.py

練習 1：抽獎與分組
"""

import random


def draw_winner(students):
    return random.choice(students)


def make_group(students, n):
    return random.sample(students, n)


def split_into_two(students):
    s = students[:]
    random.shuffle(s)
    mid = len(s) // 2
    return s[:mid], s[mid:]


if __name__ == "__main__":
    students = ["小明", "小美", "阿強", "阿花", "Amy", "John"]
    print("winner =", draw_winner(students))
    print("group =", make_group(students, 3))
    g1, g2 = split_into_two(students)
    print("group1 =", g1)
    print("group2 =", g2)
