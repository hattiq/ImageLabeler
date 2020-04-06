from PyQt5 import QtWidgets
import sys

from Ui_MainWindow import Ui_MainWindow


class ImageLabeler:

    def show(self):
        src = r"C:\Users\hatti\Desktop"

        label_classes_dict = {
            "Personal": r"C:\Users\hatti\Desktop\Personal",
            "Work": r"C:\Users\hatti\Desktop\Work"
        }

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow(MainWindow, label_classes_dict, src)
        ui.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    labeler = ImageLabeler()
    labeler.show()
