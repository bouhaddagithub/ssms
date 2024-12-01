# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Ssms
from ui_infopage import Ui_Form
import pandas as pd

class Teacher:
    def __init__(self, teacher_id, name, email):
        self.teacher_id = teacher_id
        self.name = name
        self.email = email
        self.classes = []
    def create_class(self, speciality, level, year):
        class_id = len(self.classes) + 1
        new_class = Class(class_id, speciality, level, year)
        self.classes.append(new_class)
        return new_class

    def create_group(self, _class, name, group_type):
        group_id = len(_class.groups) + 1
        new_group = Group(group_id, name, group_type, _class)
        _class.add_group(new_group)
        return new_group

    def load_students_from_excel(self, group, file_path):

        try:
            df = pd.read_excel(file_path)
            for _, row in df.iterrows():
                student = Student(row['student_id'], row['first_name'], row['last_name'])
                group.add_student(student)
        except Exception as e:
            print(f"Error loading students from Excel: {e}")

    def add_student_to_group(self, group, student):
        group.add_student(student)

    def remove_student_from_group(self, group, student):
        group.remove_student(student)

    def edit_student_in_group(self, group, student_id, new_first_name, new_last_name):
        for student in group.students:
            if student.student_id == student_id:
                student.first_name = new_first_name
                student.last_name = new_last_name
                break

    def edit_group(self, _class, group_id, new_name=None, new_group_type=None):
        for group in _class.groups:
            if group.group_id == group_id:
                if new_name:
                    group.name = new_name
                if new_group_type:
                    group.group_type = new_group_type
                break

    def delete_student_from_group(self, group, student_id):
        for student in group.students:
            if student.student_id == student_id:
                group.remove_student(student)
                break

    def delete_group(self, _class, group_id):
        for group in _class.groups:
            if group.group_id == group_id:
                _class.remove_group(group)
                break

    def __str__(self):
        return f"Teacher {self.name}, Email: {self.email}"


class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Group:
    def __init__(self, group_id, name, group_type, _class):
        self.group_id = group_id
        self.name = name
        self.group_type = group_type
        self._class = _class
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def __str__(self):
        return f"Group {self.name} ({self.group_type}) in {self._class.speciality} {self._class.level}"

class Class:
    def __init__(self, class_id, speciality, level, year):
        self.class_id = class_id
        self.speciality = speciality
        self.level = level
        self.year = year
        self.groups = []
    def add_group(self, group):
        self.groups.append(group)

    def remove_group(self, group):
        self.groups.remove(group)

    def __str__(self):
        return f"Class {self.speciality} {self.level} Year {self.year}"

class InfoPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

class Ssms(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Ssms()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.open_info_page)

    def open_info_page(self):
        self.info_page = InfoPage(self)
        self.info_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Ssms()
    widget.show()
    sys.exit(app.exec())
