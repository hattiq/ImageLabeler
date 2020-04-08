from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil
import re
import time


FILE_EXTENSION_REGEX = re.compile(r"^.+\.((?:jpg)|(?:jpeg)|(?:png))$")


class LabelClass():
    def __init__(self, name: str, dst: str, btn):
        self.name = name
        self.dst = dst
        self.btn = btn
        self.selected = False  # True: clicked , False: not clicked

    def toggle(self):
        if self.selected:
            self.selected = False
            self.btn.setStyleSheet("background-color: #bdc3c7")
        else:
            self.selected = True
            self.btn.setStyleSheet("background-color: #2ecc71")



class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, label_classes: dict, src: str):
        super(Ui_MainWindow, self).__init__()
        self.label_classes = label_classes
        self.src = src
        self.selected_btn = None
        self.next_image = None
        self.filesGen = os.walk(src)
        self.curr, self.dirs, files = self.filesGen.__next__()
        self.files = iter(files)

        self.fileCounter = 0

        self.initUi()

    def initUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)

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
            btn.setStyleSheet("background-color: #bdc3c7")
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
        self.btnNext.setStyleSheet("background-color: #3498db")
        self.btnNext.clicked.connect(self.btnNext_Click)
        self.gridLayout.addWidget(self.btnNext, 9, 1, 1, 1)

        self.Hbox = QtWidgets.QHBoxLayout(self.gridLayoutWidget)
        self.btnZoomIn = QtWidgets.QPushButton()
        self.btnZoomIn.setMaximumSize(QtCore.QSize(200, 50))
        self.btnZoomIn.setObjectName("btnZoomIn")
        self.btnZoomIn.setText("Zoom in")
        iconZoomIn = QtGui.QIcon()
        iconZoomIn.addPixmap(QtGui.QPixmap("assets/zoom-in-16.png"))
        self.btnZoomIn.setIcon(iconZoomIn)
        self.btnZoomIn.clicked.connect(self.btnZoomIn_Click)

        self.btnZoomOut = QtWidgets.QPushButton()
        self.btnZoomOut.setMaximumSize(QtCore.QSize(200, 50))
        self.btnZoomOut.setObjectName("btnbtnZoomOut")
        self.btnZoomOut.setText("Zoom out")
        iconZoomOut = QtGui.QIcon()
        iconZoomOut.addPixmap(QtGui.QPixmap("assets/zoom-out-16.png"))
        self.btnZoomOut.setIcon(iconZoomOut)
        self.btnZoomOut.clicked.connect(self.btnZoomOut_Click)

        self.btnFitWidth = QtWidgets.QPushButton()
        self.btnFitWidth.setMaximumSize(QtCore.QSize(200, 50))
        self.btnFitWidth.setObjectName("btnZoomOut")
        self.btnFitWidth.setText("Fit Size")
        iconFitWidth = QtGui.QIcon()
        iconFitWidth.addPixmap(QtGui.QPixmap("assets/fit-to-width-16.png"))
        self.btnFitWidth.setIcon(iconFitWidth)
        self.btnFitWidth.clicked.connect(self.btnFitWidth_Click)

        self.btnDeleteImage = QtWidgets.QPushButton()
        self.btnDeleteImage.setMaximumSize(QtCore.QSize(200, 50))
        self.btnDeleteImage.setObjectName("btnDeleteImage")
        self.btnDeleteImage.setText("Delete Image")
        iconDeleteImage = QtGui.QIcon()
        iconDeleteImage.addPixmap(QtGui.QPixmap("assets/remove-image-16.png"))
        self.btnDeleteImage.setIcon(iconDeleteImage)
        self.btnDeleteImage.clicked.connect(self.btnDeleteImage_Click)

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

        self.scaleFactor = 1
        self.current_pixmap = QtGui.QPixmap("assets/placeholder.jpg")

        self.statusbar.showMessage("Press Next to start.")

    def scaleImage(self, factor):
        if self.next_image is not None:
            if factor * self.scaleFactor > 2:
                self.scaleFactor = 2
            elif factor * self.scaleFactor < 1:
                self.scaleFactor = 1
            else:
                self.scaleFactor *= factor

        pixmap = self.labelImageViewer.pixmap().scaled(
            self.scaleFactor * self.current_pixmap.size().width(),
            self.scaleFactor * self.current_pixmap.size().height()
        )
        self.labelImageViewer.setPixmap(pixmap)

    def btnZoomIn_Click(self):
        if self.next_image is not None:
            self.scaleImage(1.15)

    def btnDeleteImage_Click(self):
        if self.next_image is not None:
            source = os.path.join(self.curr, self.next_image)
            os.remove(source)
            self.btnNext.click()

    def btnFitWidth_Click(self):
        if self.next_image is not None:
            max_width = self.scroll.geometry().width() - 10
            max_height = self.scroll.geometry().height() - 10

            pixmap = self.current_pixmap.scaled(max_width, max_height, QtCore.Qt.KeepAspectRatio)
            self.labelImageViewer.setPixmap(pixmap)

    def btnZoomOut_Click(self):
        if self.next_image is not None:
            self.scaleImage(0.85)

    def btnClass_Click(self):
        if self.next_image is not None:
            sender = self.sender().text()
            self.label_classes[sender].toggle()

    def btnNext_Click(self):
        try:
            if self.next_image is not None:
                isCopied = False
                source = os.path.join(self.curr, self.next_image)
                for label_btn in self.label_classes:
                    if self.label_classes[label_btn].selected:
                        destination = os.path.join(
                            self.label_classes[label_btn].dst,
                            f'{Ui_MainWindow.__current_milli_time()}{self.fileCounter} {self.next_image}')
                        shutil.copyfile(source, destination)
                        self.fileCounter += 1
                        isCopied = True
                        self.label_classes[label_btn].toggle()
                if isCopied:
                    os.remove(source)

            self.next_image = next(self.files)
            while not FILE_EXTENSION_REGEX.match(self.next_image):
                self.next_image = next(self.files)
        except StopIteration:
            try:
                self.next_image = None
                self.labelImageViewer.setPixmap(QtGui.QPixmap("assets/placeholder.jpg"))
                self.current_pixmap = QtGui.QPixmap("assets/placeholder.jpg")
                self.statusbar.showMessage("No more images (jpg,jpeg,png) in current folder ("+self.curr +
                                           "). click next to walk to next directory")

                files = []
                while not files:
                    self.curr, self.dirs, files = self.filesGen.__next__()
                self.files = iter(files)

            except OSError:
                self.statusbar.showMessage("")
            except StopIteration:
                self.statusbar.showMessage("Finished. Every file traversed successfully.")
                pass
        else:
            max_width = self.scroll.geometry().width()-10
            max_height = self.scroll.geometry().height()-10

            self.current_pixmap = QtGui.QPixmap(os.path.join(self.curr, self.next_image))

            if self.current_pixmap.width() > max_width or self.current_pixmap.height() > max_height:
                self.current_pixmap = self.current_pixmap.scaled(max_width, max_height, QtCore.Qt.KeepAspectRatio)

            self.labelImageViewer.setPixmap(self.current_pixmap)
            self.scaleFactor = 1

        if self.next_image is not None:
            self.statusbar.showMessage(f"Current File: {self.curr}{os.path.sep}{self.next_image}")

    @staticmethod
    def __current_milli_time() -> int:
        return int(round(time.time() * 1000))
