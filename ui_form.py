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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Ssms(object):
    def setupUi(self, Ssms):
        if not Ssms.objectName():
            Ssms.setObjectName(u"Ssms")
        Ssms.resize(1316, 675)
        Ssms.setMinimumSize(QSize(100, 0))
        self.verticalLayoutWidget = QWidget(Ssms)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1352, 681))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.enter1 = QPushButton(self.verticalLayoutWidget)
        self.enter1.setObjectName(u"enter1")
        self.enter1.setMaximumSize(QSize(1350, 600))
        icon = QIcon()
        icon.addFile(u"../../../../../OneDrive/Pictures/imagecls.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.enter1.setIcon(icon)
        self.enter1.setIconSize(QSize(1350, 1350))

        self.verticalLayout.addWidget(self.enter1)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(1350, 100))
        self.pushButton.setStyleSheet(u"color: rgb(85, 170, 0) ;\n"
"font: 700 28pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Ssms)

        QMetaObject.connectSlotsByName(Ssms)
    # setupUi

    def retranslateUi(self, Ssms):
        Ssms.setWindowTitle(QCoreApplication.translate("Ssms", u"Ssms", None))
        self.enter1.setText("")
        self.pushButton.setText(QCoreApplication.translate("Ssms", u"->", None))
    # retranslateUi

