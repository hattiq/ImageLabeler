from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


class LabelClass():
    def __init__(self, name: str, dst: str, btn):
        self.name = name
        self.dst = dst
        self.btn = btn
        self.selected = False  # True: clicked , False: not clicked

    def toggleOn(self, ):
        self.selected = True
        self.btn.setStyleSheet("background-color: red")

    def toggleOff(self, ):
        self.selected = False
        self.btn.setStyleSheet("background-color: yellow")


class Ui_MainWindow(QtWidgets.QWidget):

    def __init__(self, MainWindow, label_classes: dict, src: str):
        super(Ui_MainWindow, self).__init__()
        self.label_classes = label_classes
        self.src = src
        self.selected_btn = None
        self.setupUi(MainWindow)
        self.files = iter(os.listdir(self.src))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.setLayout(self.gridLayout)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        row = 0
        for c in self.label_classes:
            btn = QtWidgets.QPushButton()
            btn.setSizePolicy(sizePolicy)
            btn.setMaximumSize(QtCore.QSize(200, 50))
            btn.setObjectName("btn" + c)
            btn.setText(c)
            btn.clicked.connect(self.btnClass_Click)
            self.gridLayout.addWidget(btn, row, 1, 1, 1)
            self.label_classes[c] = LabelClass(c, self.label_classes[c], btn)
            row += 1

        self.btnNext = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.btnNext.setSizePolicy(sizePolicy)
        self.btnNext.setMaximumSize(QtCore.QSize(200, 50))
        self.btnNext.setObjectName("btnNext")
        self.btnNext.setText("Next")
        self.btnNext.clicked.connect(self.btnNext_Click)
        self.gridLayout.addWidget(self.btnNext, 9, 1, 1, 1)

        self.labelImageViewer = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.labelImageViewer.setSizePolicy(sizePolicy)
        self.labelImageViewer.setText("")
        self.labelImageViewer.setPixmap(QtGui.QPixmap("placeholder.jpg"))
        self.labelImageViewer.setMaximumSize(QtCore.QSize(1000, 1000))
        self.labelImageViewer.setObjectName("labelImageViewer")
        self.gridLayout.addWidget(self.labelImageViewer, 0, 0, 10, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def btnClass_Click(self):
        if self.next_image is not None:
            sender = self.sender().text()
            if self.selected_btn is not None:
                self.label_classes[self.selected_btn].toggleOff()
            self.selected_btn = sender
            self.label_classes[self.selected_btn].toggleOn()

    def btnNext_Click(self):
        try:

            if self.selected_btn is not None:
                source = os.path.join(self.src, self.next_image)
                destination = os.path.join(self.src, self.label_classes[self.selected_btn].dst, self.next_image)
                os.rename(source, destination)

            self.next_image = next(self.files)
            while not (self.next_image.endswith(".jpg") or self.next_image.endswith(".jpeg") or self.next_image.endswith(".png")):
                self.next_image = next(self.files)
        except StopIteration:
            self.next_image = None
        except OSError:
            pass
        else:

            pixmap = QtGui.QPixmap(os.path.join(self.src, self.next_image))
            pixmap = pixmap.scaled(750, 750, QtCore.Qt.KeepAspectRatio)
            self.labelImageViewer.setPixmap(pixmap)
