# This Python file uses the following encoding: utf-8
import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget,QListWidgetItem, QDialog, QFormLayout, QLineEdit,QDialogButtonBox,QComboBox,QFileDialog,QTableWidgetItem,QMessageBox
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Ssms
from ui_infopage import Ui_Form
import pandas as pd
import re

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
        self.load_classes()
        self.ui.classlist.currentIndexChanged.connect(self.on_class_selected)
        self.ui.group_combo.currentIndexChanged.connect(lambda:
            self.on_group_selected(self.ui.group_combo.currentData()))




        self.ui.home.clicked.connect(self.switch_to_second_tab)
        self.ui.cls.clicked.connect(self.switch_to_first_tab)
        self.ui.loadstudentlistb.clicked.connect(self.load_students_from_excel)
        self.ui.addclass.clicked.connect(self.create_class)
        self.ui.create_group_button.clicked.connect(self.create_group)
        self.ui.save_changes_button.clicked.connect(self.save_edited_students)
        self.ui.add_row_button.clicked.connect(self.add_row_to_table)



    def database_setup(self):
        """Set up the SQLite database and create the necessary table."""
        self.conn = sqlite3.connect("school_management.db")
        self.cursor = self.conn.cursor()

        # Create classes table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS classes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                speciality TEXT NOT NULL,
                level_type TEXT NOT NULL,
                level TEXT NOT NULL,
                year TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
         CREATE TABLE IF NOT EXISTS groups (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             class_id INTEGER NOT NULL,
             name TEXT NOT NULL,
             type TEXT NOT NULL,
             FOREIGN KEY (class_id) REFERENCES classes (id)
         )
         """)
        self.cursor.execute("""
             CREATE TABLE IF NOT EXISTS students (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 group_id INTEGER NOT NULL,
                 first_name TEXT NOT NULL,
                 last_name TEXT NOT NULL,
                 FOREIGN KEY (group_id) REFERENCES groups (id)
             )
         """)
        self.cursor.execute("""
                PRAGMA table_info(classes)
            """)
        existing_columns = [row[1] for row in self.cursor.fetchall()]
        if 'name' not in existing_columns:
            self.cursor.execute("ALTER TABLE classes ADD COLUMN name TEXT")
        if 'level_type' not in existing_columns:
            self.cursor.execute("ALTER TABLE classes ADD COLUMN level_type TEXT")
        self.conn.commit()
    def add_row_to_table(self):
        current_row_count = self.ui.student_table.rowCount()
        self.ui.student_table.insertRow(current_row_count)  # Add an empty row

    def on_group_selected(self, group_id):
        if group_id:
            self.load_students(group_id)  # Load students for the selected group
        else:
            self.ui.student_table.setRowCount(0)  # Clear table for a new group




    def switch_to_first_tab(self):
        self.ui.tabWidget.setCurrentIndex(0)
    def switch_to_second_tab(self):
        self.ui.tabWidget.setCurrentIndex(2)

    def on_class_selected(self):
        selected_index = self.ui.classlist.currentIndex()
        if selected_index != -1:
            class_id = self.ui.classlist.itemData(selected_index, Qt.UserRole)
            if class_id is not None:
                self.load_groups(class_id)

            self.ui.tabWidget.setCurrentIndex(1)



    def load_classes(self):
        """Load all classes from the database into the list widget."""
        self.ui.classlist.clear()
        self.cursor.execute("SELECT id, name, level_type FROM classes")
        rows = self.cursor.fetchall()
        for class_id, name,level_type in rows:
            #class_id, name, speciality, level, year = row
            class_info =  f"{name} ({level_type})"
            self.ui.classlist.addItem(class_info, class_id)
    def load_groups(self, class_id):
        self.ui.group_combo.clear()
        self.cursor.execute("SELECT id, name, type FROM groups WHERE class_id = ?", (class_id,))
        groups = self.cursor.fetchall()

        for group_id, name, group_type in groups:
            self.ui.group_combo.addItem(f"{name} ({group_type})", group_id)

        if groups:
            first_group_id = groups[0][0]
            self.ui.group_combo.setCurrentIndex(0)
            self.on_group_selected(first_group_id)
    def save_students_to_group(self, group_id):
        for row in range(self.ui.student_table.rowCount()):
            first_name_item = self.ui.student_table.item(row, 0)
            last_name_item = self.ui.student_table.item(row, 1)

                    # Ensure the cells are not empty
            if first_name_item and last_name_item:
                first_name = first_name_item.text()
                last_name = last_name_item.text()

                        # Save to the database
                self.cursor.execute("""
                    INSERT INTO students (group_id, first_name, last_name)
                    VALUES (?, ?, ?)
                """, (group_id, first_name, last_name))
        self.conn.commit()

    def save_edited_students(self):

        selected_group_index = self.ui.group_combo.currentIndex()
        if selected_group_index == -1:
            QMessageBox.warning(self, "No Group Selected", "Please select a group first.")
            return

        group_id = self.ui.group_combo.currentData()


        self.cursor.execute("DELETE FROM students WHERE group_id = ?", (group_id,))


        row_count = self.ui.student_table.rowCount()
        for row in range(row_count):
            first_name_item = self.ui.student_table.item(row, 0)
            last_name_item = self.ui.student_table.item(row, 1)

            if first_name_item and last_name_item:
                first_name = first_name_item.text().strip()
                last_name = last_name_item.text().strip()
                self.cursor.execute("""
                    INSERT INTO students (group_id, first_name, last_name)
                    VALUES (?, ?, ?)
                """, (group_id, first_name, last_name))

        self.conn.commit()
        QMessageBox.information(self, "Success", "Changes saved successfully.")
        self.load_students(group_id)  # Refresh the table

    def create_class(self):
        """Open a dialog to create a new class."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Create New Class")
        dialog_layout = QFormLayout(dialog)

        # Inputs
        name_input = QLineEdit()
        speciality_input = QComboBox()
        speciality_input.addItems(["Math", "Info"])

        level_type_input = QComboBox()
        level_type_input.addItems(["LMD", "ING"])

        level_input = QComboBox()

        year_input = QLineEdit()
        year_input.setPlaceholderText("e.g., 2023/2024")
        def update_level_options():
                speciality = speciality_input.currentText()
                level_type = level_type_input.currentText()
                level_input.clear()

                if speciality == "Info":
                    if level_type == "LMD":
                        level_input.addItems(["L1", "L2", "L3", "M1", "M2"])
                    elif level_type == "ING":
                        level_input.addItems(["ING1", "ING2", "ING3", "ING4", "ING5"])
                elif speciality == "Math":
                    level_input.addItems(["L1", "L2", "L3", "M1", "M2"])

        speciality_input.currentIndexChanged.connect(update_level_options)
        level_type_input.currentIndexChanged.connect(update_level_options)
        dialog_layout.addRow("Class Name:", name_input)
        dialog_layout.addRow("Speciality:", speciality_input)
        dialog_layout.addRow("Level Type:", level_type_input)
        dialog_layout.addRow("Level:", level_input)
        dialog_layout.addRow("Year:", year_input)

        # Dialog buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        dialog_layout.addWidget(button_box)

        # Show dialog and get result
        if dialog.exec() == QDialog.Accepted:
            name = name_input.text().strip()
            speciality = speciality_input.currentText()
            level_type = level_type_input.currentText()
            level = level_input.currentText()
            year = year_input.text().strip()



            print(f"Name: {name}")
            print(f"Speciality: {speciality}")
            print(f"Level Type: {level_type}")
            print(f"Level: {level}")
            print(f"Year: {year}")
            if not self.validate_year_format(year):
                QMessageBox.warning(self, "Invalid Year", "Year must be in the format YYYY/YYYY (e.g., 2023/2024).")
                return

            if name and speciality and level and level_type:
                self.save_class_to_db(name,speciality, level, year, level_type)
                self.load_classes()
            else:
                print("Invalid input. Please fill out all fields correctly.")

    def validate_year_format(self, year):
        return bool(re.match(r"^\d{4}/\d{4}$", year))

    def load_students(self, group_id):

        self.ui.student_table.setRowCount(0)  # Clear existing rows
        self.cursor.execute("SELECT id, first_name, last_name FROM students WHERE group_id = ?", (group_id,))
        students = self.cursor.fetchall()

        for row_idx, (student_id, first_name, last_name) in enumerate(students):
            self.ui.student_table.insertRow(row_idx)
            self.ui.student_table.setItem(row_idx, 0, QTableWidgetItem(first_name))
            self.ui.student_table.setItem(row_idx, 1, QTableWidgetItem(last_name))


    def load_students_from_excel(self):
                # Ensure a class is selected
        selected_index = self.ui.classlist.currentIndex()
        if selected_index == -1:
            QMessageBox.warning(self, "No Class Selected", "Please select a class before loading students.")
            return

        class_id = self.ui.classlist.itemData(selected_index, Qt.UserRole)

                # Prompt for group details
        dialog = QDialog(self)
        dialog.setWindowTitle("Create Group")
        dialog_layout = QFormLayout(dialog)

        group_name_input = QLineEdit()
        group_type_input = QComboBox()
        group_type_input.addItems(["TD", "TP"])
        dialog_layout.addRow("Group Name:", group_name_input)
        dialog_layout.addRow("Group Type:", group_type_input)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        dialog_layout.addWidget(button_box)

        if dialog.exec() != QDialog.Accepted:
            return

        group_name = group_name_input.text()
        group_type = group_type_input.currentText()

        if not group_name:
            QMessageBox.warning(self, "Invalid Input", "Group name cannot be empty.")
            return

                # Save group to database
        self.cursor.execute("""
            INSERT INTO groups (class_id, name, type)
            VALUES (?, ?, ?)
        """, (class_id, group_name, group_type))
        group_id = self.cursor.lastrowid  # Get the ID of the newly created group
        self.conn.commit()


        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xlsx)")
        if not file_path:
            return

        try:
                    # Load data from Excel
            data = pd.read_excel(file_path)

                    # Assuming the columns are named 'Name' and 'Surname' or 'nom' and 'prenom'
            name_column = 'Name'
            surname_column = 'Surname'

            if 'nom' in data.columns and 'prenom' in data.columns:
                name_column = 'nom'
                surname_column = 'prenom'

                    # Insert students into the database
            for _, row in data.iterrows():
                first_name = row[name_column]
                last_name = row[surname_column]
                self.cursor.execute("""
                    INSERT INTO students (group_id, first_name, last_name)
                    VALUES (?, ?, ?)
                """, (group_id, first_name, last_name))

            self.conn.commit()

            QMessageBox.information(self, "Success", "Students have been added to the group successfully.")
            #self.load_groups(class_id)  # Refresh group list
            self.load_students(group_id)  # Refresh the student table

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")


    def save_class_to_db(self, name,  speciality, level, year,level_type):
        """Save a new class to the database."""
        self.cursor.execute("""
            INSERT INTO classes (name, speciality, level_type, level, year)
            VALUES (?, ?, ?, ?, ?)
        """, (name, speciality, level_type, level, year))
        self.conn.commit()

    def create_group(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Create Group")
        dialog_layout = QFormLayout(dialog)

            # Inputs
        name_input = QLineEdit()
        type_input = QComboBox()
        type_input.addItems(["TD", "TP"])
        dialog_layout.addRow("Group Name:", name_input)
        dialog_layout.addRow("Group Type:", type_input)

            # Dialog Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        dialog_layout.addWidget(button_box)

            # Show dialog
        if dialog.exec() == QDialog.Accepted:
            name = name_input.text()
            group_type = type_input.currentText()
            class_id = self.ui.classlist.currentData()
            if not class_id:
                       QMessageBox.warning(self, "Error", "No class selected. Please select a class.")
                       return

            if name and group_type:
                self.cursor.execute("""
                    INSERT INTO groups (class_id, name, type)
                    VALUES (?, ?, ?)
                 """, (class_id, name, group_type))
                self.conn.commit()
                self.load_groups(class_id)  # Refresh group list
            else:
                print("Invalid input. Please fill all fields.")

    def closeEvent(self, event):
        """Close the database connection when the app is closed."""
        self.conn.close()
        super().closeEvent(event)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Ssms()
    widget.show()
    sys.exit(app.exec())
