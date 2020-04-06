from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


class LabelClass():
    def __init__(self, name: str, dst: str, btn):
        self.name = name
        self.dst = dst
        self.btn = btn
        self.selected = False  # True: clicked , False: not clicked

    def toggleOn(self):
        self.selected = True
        self.btn.setStyleSheet("background-color: red")

    def toggleOff(self):
        self.selected = False
        self.btn.setStyleSheet("background-color: yellow")


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, label_classes: dict, src: str):
        super(Ui_MainWindow, self).__init__()
        self.label_classes = label_classes
        self.src = src
        self.selected_btn = None
        self.files = iter(os.listdir(self.src))
        self.initUi()

    def initUi(self):
        self.setObjectName("MainWindow")
        self.resize(1000, 750)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")

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

        self.Hbox = QtWidgets.QHBoxLayout(self.gridLayoutWidget)
        self.btnZoomIn = QtWidgets.QPushButton()
        self.btnZoomIn.setMaximumSize(QtCore.QSize(200, 50))
        self.btnZoomIn.setObjectName("btnbtnZoomIn")
        self.btnZoomIn.setText("")
        iconZoomIn = QtGui.QIcon()
        iconZoomIn.addPixmap(QtGui.QPixmap("assets/zoom-in-16.png"))
        self.btnZoomIn.setIcon(iconZoomIn)
        self.btnZoomIn.setStyleSheet("background-color: transparent")

        self.btnZoomOut = QtWidgets.QPushButton()
        self.btnZoomOut.setMaximumSize(QtCore.QSize(200, 50))
        self.btnZoomOut.setObjectName("btnbtnZoomOut")
        self.btnZoomOut.setText("")
        iconZoomOut = QtGui.QIcon()
        iconZoomOut.addPixmap(QtGui.QPixmap("assets/zoom-out-16.png"))
        self.btnZoomOut.setIcon(iconZoomOut)
        self.btnZoomOut.setStyleSheet("background-color: transparent")

        self.btnFitWidth = QtWidgets.QPushButton()
        self.btnFitWidth.setMaximumSize(QtCore.QSize(200, 50))
        self.btnFitWidth.setObjectName("btnbtnZoomOut")
        self.btnFitWidth.setText("")
        iconFitWidth = QtGui.QIcon()
        iconFitWidth.addPixmap(QtGui.QPixmap("assets/fit-to-width-16.png"))
        self.btnFitWidth.setIcon(iconFitWidth)
        self.btnFitWidth.setStyleSheet("background-color: transparent")

        self.btnDeleteImage = QtWidgets.QPushButton()
        self.btnDeleteImage.setMaximumSize(QtCore.QSize(200, 50))
        self.btnDeleteImage.setObjectName("btnbtnZoomOut")
        self.btnDeleteImage.setText("")
        iconDeleteImage = QtGui.QIcon()
        iconDeleteImage.addPixmap(QtGui.QPixmap("assets/remove-image-16.png"))
        self.btnDeleteImage.setIcon(iconDeleteImage)
        self.btnDeleteImage.setStyleSheet("background-color: transparent")

        self.Hbox.addWidget(self.btnZoomIn)
        self.Hbox.addWidget(self.btnFitWidth)
        self.Hbox.addWidget(self.btnZoomOut)
        self.Hbox.addWidget(self.btnDeleteImage)
        widget = QtWidgets.QWidget()
        widget.setLayout(self.Hbox)
        self.gridLayout.addWidget(widget, 10, 0, 1, 1)

        self.labelImageViewer = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.labelImageViewer.setSizePolicy(sizePolicy)
        self.labelImageViewer.setText("")
        self.labelImageViewer.setPixmap(QtGui.QPixmap("assets/placeholder.jpg"))
        self.labelImageViewer.setObjectName("labelImageViewer")
        self.labelImageViewer.setAlignment(QtCore.Qt.AlignCenter)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.labelImageViewer)

        self.gridLayout.addWidget(self.scroll, 0, 0, 10, 1)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.gridLayout)
        self.setCentralWidget(self.widget)
        self.widget.show()
        self.setWindowTitle("Image Labeler")

    def wheelEvent(self, a0: QtGui.QWheelEvent) -> None:
        self.scaleImage(1.25)

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.labelImageViewer.resize(self.scaleFactor * self.labelImageViewer.pixmap().size())

        self.adjustScrollBar(self.scroll.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scroll.verticalScrollBar(), factor)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))

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
            self.labelImageViewer.setPixmap(QtGui.QPixmap("placeholder.jpg"))
        except OSError:
            pass
        else:

            max_width = self.labelImageViewer.geometry().width()
            max_height = self.labelImageViewer.geometry().height()

            pixmap = QtGui.QPixmap(os.path.join(self.src, self.next_image))

            if pixmap.width() > max_width or pixmap.height() > max_height:
                pixmap = pixmap.scaled(max_width, max_height, QtCore.Qt.KeepAspectRatio)

            self.labelImageViewer.setPixmap(pixmap)
