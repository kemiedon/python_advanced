"""
資料模型模組
定義學生和科目的類別
"""


class Student:
    """學生類別"""

    def __init__(self, student_id=None, name=None, age=None, email=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"學生 ID: {self.student_id}, 姓名: {self.name}, 年齡: {self.age}, Email: {self.email}"

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.age}, {self.email})"

    def to_dict(self):
        """轉換為字典格式（用於 JSON）"""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data):
        """從字典建立 Student 物件"""
        return cls(
            student_id=data.get("student_id"),
            name=data.get("name"),
            age=data.get("age"),
            email=data.get("email"),
        )


class Subject:
    """科目類別"""

    def __init__(self, subject_id=None, subject_name=None, credits=None):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.credits = credits

    def __str__(self):
        return f"科目 ID: {self.subject_id}, 科目名稱: {self.subject_name}, 學分: {self.credits}"

    def __repr__(self):
        return f"Subject({self.subject_id}, {self.subject_name}, {self.credits})"

    def to_dict(self):
        """轉換為字典格式（用於 JSON）"""
        return {
            "subject_id": self.subject_id,
            "subject_name": self.subject_name,
            "credits": self.credits,
        }

    @classmethod
    def from_dict(cls, data):
        """從字典建立 Subject 物件"""
        return cls(
            subject_id=data.get("subject_id"),
            subject_name=data.get("subject_name"),
            credits=data.get("credits"),
        )


class Grade:
    """成績類別"""

    def __init__(self, grade_id=None, student_id=None, subject_id=None, score=None):
        self.grade_id = grade_id
        self.student_id = student_id
        self.subject_id = subject_id
        self.score = score

    def __str__(self):
        return f"成績 ID: {self.grade_id}, 學生 ID: {self.student_id}, 科目 ID: {self.subject_id}, 分數: {self.score}"

    def __repr__(self):
        return f"Grade({self.grade_id}, {self.student_id}, {self.subject_id}, {self.score})"

    def to_dict(self):
        """轉換為字典格式（用於 JSON）"""
        return {
            "grade_id": self.grade_id,
            "student_id": self.student_id,
            "subject_id": self.subject_id,
            "score": self.score,
        }

    @classmethod
    def from_dict(cls, data):
        """從字典建立 Grade 物件"""
        return cls(
            grade_id=data.get("grade_id"),
            student_id=data.get("student_id"),
            subject_id=data.get("subject_id"),
            score=data.get("score"),
        )
