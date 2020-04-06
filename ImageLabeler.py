import sys
import argparse
import os

from PyQt5 import QtWidgets
from Ui_MainWindow import Ui_MainWindow


LABEL_CLASSES_DIRECTORIES = {
            "Red": r"D:\FYP\Demo\sorted\red",
            "Green": r"D:\FYP\Demo\sorted\green",
            "Blue": r"D:\FYP\Demo\sorted\blue",
        }


class ImageLabeler:
    """
    App to copy images from one folder to multiple folders. This could be effectively used as a sorting and
    labeling technique.
    """
    @staticmethod
    def show(src):
        """
        Initialize and start app.

        :param src: source directory from which images are to be taken; subdirectories included.
        :return:
        """

        label_classes_dict = LABEL_CLASSES_DIRECTORIES

        app = QtWidgets.QApplication(sys.argv)
        ui = Ui_MainWindow(label_classes_dict, src)
        ui.show()
        sys.exit(app.exec_())


def __init_arg_parser() -> argparse.ArgumentParser:
    """
    Configures an ArgumentParser with arguments needed for ImageLabeler app.

    :return: A Configured argparse.ArgumentParser
    """

    parser = argparse.ArgumentParser(
        description='Run this app to copy a single file into multiple folders as a labeling technique.')

    parser.add_argument('source_directory',
                        type=str,
                        help='Directory from where images will we be taken.'
                        'Subdirectories included.')

    return parser


if __name__ == "__main__":
    arg_parser = __init_arg_parser()
    args = arg_parser.parse_args()

    labeler = ImageLabeler()

    assert os.path.isdir(args.source_directory), f'Directory "{args.source_directory} does not exist"'

    labeler.show(src=args.source_directory)
