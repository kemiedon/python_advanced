"""example_os_pathlib.py

示範 os / pathlib 模組
"""

import os
from pathlib import Path


def demo():
    print("cwd =", os.getcwd())
    p = Path(".")
    print("list files =", [x.name for x in p.iterdir() if x.is_file()])
    d = Path("test_dir")
    d.mkdir(exist_ok=True)
    print("ensure dir test_dir created")


if __name__ == "__main__":
    demo()
