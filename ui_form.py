# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Ssms(object):
    def setupUi(self, Ssms):
        if not Ssms.objectName():
            Ssms.setObjectName(u"Ssms")
        Ssms.resize(1316, 675)
        Ssms.setMinimumSize(QSize(854, 480))
        Ssms.setStyleSheet(u"/* General Application Background */\n"
"QWidget {\n"
"    background-color: #000814; /* Primary Dark */\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QPushButton {\n"
"    background-color: #003566; /* Tertiary Dark */\n"
"    border: 2px solid #001d3d; /* Secondary Dark */\n"
"    border-radius: 8px;\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"    padding: 10px 20px;\n"
"    font-weight: bold;\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffc300; /* Accent Bright */\n"
"    color: #001d3d; /* Secondary Dark */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ffd60a; /* Highlight Bright */\n"
"    color: #000814; /* Primary Dark */\n"
"}\n"
"\n"
"/* Labels */\n"
"QLabel {\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Line Edits */\n"
"QLineEdit"
                        " {\n"
"    background-color: #001d3d; /* Secondary Dark */\n"
"    border: 2px solid #003566; /* Tertiary Dark */\n"
"    border-radius: 5px;\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #ffc300; /* Accent Bright */\n"
"}\n"
"\n"
"/* Text Edits */\n"
"QTextEdit, QPlainTextEdit {\n"
"    background-color: #001d3d; /* Secondary Dark */\n"
"    border: 2px solid #003566; /* Tertiary Dark */\n"
"    border-radius: 5px;\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: #001d3d; /* Secondary Dark */\n"
"    border: 2px solid #003566; /* Tertiary Dark */\n"
"    border-radius: 5px;\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background-color: #003566; /* Tertiary Dark */\n"
"}\n"
"\n"
"QComboBox QAbstractItemV"
                        "iew {\n"
"    background-color: #001d3d; /* Secondary Dark */\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"    selection-background-color: #ffc300; /* Accent Bright */\n"
"    selection-color: #001d3d; /* Secondary Dark */\n"
"}\n"
"\n"
"/* Scrollbars */\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    background: #001d3d; /* Secondary Dark */\n"
"    border: none;\n"
"    width: 12px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: #ffc300; /* Accent Bright */\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: none;\n"
"}\n"
"\n"
"/* Progress Bars */\n"
"QProgressBar {\n"
"    background-color: #001d3d; /* Secondary Dark */\n"
"    border: 2px solid #003566; /* Tertiary Dark */\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #ffc300; /* Accent Bright */\n"
""
                        "    width: 20px;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"/* Group Boxes */\n"
"QGroupBox {\n"
"    border: 2px solid #003566; /* Tertiary Dark */\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 10px;\n"
"    background-color: #000814; /* Primary Dark */\n"
"}\n"
"\n"
"/* Tooltips */\n"
"QToolTip {\n"
"    background-color: #ffc300; /* Accent Bright */\n"
"    color: #001d3d; /* Secondary Dark */\n"
"    border: 1px solid #003566; /* Tertiary Dark */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Menus */\n"
"QMenu {\n"
"    background-color: #001d3d; /* Secondary Dark */\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"    border: 2px solid #003566; /* Tertiary Dark */\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 5px 20px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"   "
                        " background-color: #ffc300; /* Accent Bright */\n"
"    color: #001d3d; /* Secondary Dark */\n"
"}\n"
"\n"
"/* Tabs */\n"
"QTabWidget::pane {\n"
"    border: 2px solid #003566; /* Tertiary Dark */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #001d3d; /* Secondary Dark */\n"
"    border: 1px solid #003566; /* Tertiary Dark */\n"
"    padding: 10px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #003566; /* Tertiary Dark */\n"
"    color: #ffd60a; /* Highlight Bright */\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Ssms)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Ssms)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.home = QPushButton(self.frame)
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(0, 50))
        self.home.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"assets/house-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home.setIcon(icon)

        self.verticalLayout.addWidget(self.home)

        self.cls = QPushButton(self.frame)
        self.cls.setObjectName(u"cls")
        self.cls.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.cls)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(5, 40)

        self.horizontalLayout.addWidget(self.frame)

        self.tabWidget = QTabWidget(Ssms)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.addclass = QPushButton(self.tab)
        self.addclass.setObjectName(u"addclass")
        self.addclass.setGeometry(QRect(10, 220, 241, 51))
        self.classlist = QComboBox(self.tab)
        self.classlist.setObjectName(u"classlist")
        self.classlist.setGeometry(QRect(10, 20, 881, 161))
        self.tabWidget.addTab(self.tab, "")
        self.secondtab = QWidget()
        self.secondtab.setObjectName(u"secondtab")
        self.student_table = QTableWidget(self.secondtab)
        if (self.student_table.columnCount() < 2):
            self.student_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.student_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.student_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.student_table.setObjectName(u"student_table")
        self.student_table.setGeometry(QRect(30, 210, 341, 301))
        self.student_table.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.create_group_button = QPushButton(self.secondtab)
        self.create_group_button.setObjectName(u"create_group_button")
        self.create_group_button.setGeometry(QRect(30, 530, 161, 51))
        self.loadstudentlistb = QPushButton(self.secondtab)
        self.loadstudentlistb.setObjectName(u"loadstudentlistb")
        self.loadstudentlistb.setGeometry(QRect(30, 160, 151, 41))
        self.group_combo = QComboBox(self.secondtab)
        self.group_combo.setObjectName(u"group_combo")
        self.group_combo.setGeometry(QRect(30, 60, 991, 81))
        self.save_changes_button = QPushButton(self.secondtab)
        self.save_changes_button.setObjectName(u"save_changes_button")
        self.save_changes_button.setGeometry(QRect(230, 530, 131, 51))
        self.add_row_button = QPushButton(self.secondtab)
        self.add_row_button.setObjectName(u"add_row_button")
        self.add_row_button.setGeometry(QRect(390, 210, 83, 51))
        self.tabWidget.addTab(self.secondtab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Ssms)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Ssms)
    # setupUi

    def retranslateUi(self, Ssms):
        Ssms.setWindowTitle(QCoreApplication.translate("Ssms", u"Ssms", None))
        self.home.setText(QCoreApplication.translate("Ssms", u"  HOME       ", None))
        self.cls.setText(QCoreApplication.translate("Ssms", u"CLASS", None))
        self.pushButton_6.setText(QCoreApplication.translate("Ssms", u"Calender", None))
        self.pushButton_4.setText(QCoreApplication.translate("Ssms", u"Settings", None))
        self.addclass.setText(QCoreApplication.translate("Ssms", u"cretae class", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Ssms", u"Tab 1", None))
        ___qtablewidgetitem = self.student_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Ssms", u"Name", None));
        ___qtablewidgetitem1 = self.student_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Ssms", u"Surname", None));
        self.create_group_button.setText(QCoreApplication.translate("Ssms", u"create groupe", None))
        self.loadstudentlistb.setText(QCoreApplication.translate("Ssms", u"Load students", None))
        self.save_changes_button.setText(QCoreApplication.translate("Ssms", u"save", None))
        self.add_row_button.setText(QCoreApplication.translate("Ssms", u"add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.secondtab), QCoreApplication.translate("Ssms", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Ssms", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Ssms", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Ssms", u"Page", None))
    # retranslateUi

