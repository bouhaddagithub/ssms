# This Python file uses the following encoding: utf-8
import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget,QListWidgetItem, QDialog, QFormLayout, QLineEdit,QDialogButtonBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Ssms
from ui_infopage import Ui_Form
#import pandas as pd

"""class Teacher:
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
"""

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

class Noclass:
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


class Ssms(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Ssms()
        self.ui.setupUi(self)

        #self.ui.pushButton.clicked.connect(self.open_info_page)

        self.database_setup()  # Setup database
        self.load_classes()  # Load classes into the list widget
        self.ui.classlist.currentIndexChanged.connect(self.on_class_selected)

        # Connect UI signals to logic
        self.ui.addclass.clicked.connect(self.create_class)

    def database_setup(self):
        """Set up the SQLite database and create the necessary table."""
        self.conn = sqlite3.connect("school_management.db")
        self.cursor = self.conn.cursor()

        # Create classes table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                speciality TEXT NOT NULL,
                level TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def on_class_selected(self):
        selected_index = self.ui.classlist.currentIndex()
        if selected_index != -2:
            self.ui.tabWidget.setCurrentIndex(selected_index)

    def load_classes(self):
        """Load all classes from the database into the list widget."""
        self.ui.classlist.clear()
        self.cursor.execute("SELECT * FROM classes")
        rows = self.cursor.fetchall()
        for row in rows:
            class_id, speciality, level, year = row
            class_info = f"{speciality} - {level} - {year}"
            self.ui.classlist.addItem(class_info)

    def create_class(self):
        """Open a dialog to create a new class."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Create New Class")
        dialog_layout = QFormLayout(dialog)

        # Inputs
        speciality_input = QLineEdit()
        level_input = QLineEdit()
        year_input = QLineEdit()
        dialog_layout.addRow("Speciality:", speciality_input)
        dialog_layout.addRow("Level:", level_input)
        dialog_layout.addRow("Year:", year_input)

        # Dialog buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        dialog_layout.addWidget(button_box)

        # Show dialog and get result
        if dialog.exec() == QDialog.Accepted:
            speciality = speciality_input.text()
            level = level_input.text()
            year = year_input.text()

            if speciality and level and year.isdigit():
                self.save_class_to_db(speciality, level, int(year))
                self.load_classes()
            else:
                print("Invalid input. Please fill out all fields correctly.")

    def save_class_to_db(self, speciality, level, year):
        """Save a new class to the database."""
        self.cursor.execute("""
            INSERT INTO classes (speciality, level, year)
            VALUES (?, ?, ?)
        """, (speciality, level, year))
        self.conn.commit()

    def closeEvent(self, event):
        """Close the database connection when the app is closed."""
        self.conn.close()
        super().closeEvent(event)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Ssms()
    widget.show()
    sys.exit(app.exec())
