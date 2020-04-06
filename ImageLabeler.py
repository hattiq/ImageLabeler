import sys
import argparse
import os

from PyQt5 import QtWidgets
from Ui_MainWindow import Ui_MainWindow


LABEL_CLASSES_DIRECTORIES = {
            "Red": r".\Demo\sorted\red",
            "Green": r".\Demo\sorted\green",
            "Blue": r".\Demo\sorted\blue",
        }


class ImageLabeler:
    """
    App to copy images from one folder to multiple folders. This could be effectively used as a sorting and
    labeling technique.
    """
    @staticmethod
    def show(src, label_classes_dict):
        """
        Initialize and start app.

        :param src: source directory from which images are to be taken; subdirectories included.
        :label_classes_dict: A dict where keys are class names and values are directory paths.
        :return:
        """

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


def __create_if_not_exist_directories(dictionary: dict):
    """
    Creates directories out of the values of dictionary.

    If directory exists, that's okay. Otherwise it is created.

    :param dictionary: key value pairs, where values are directory paths.
    :return: None.
    """
    for key, value in dictionary.items():
        os.makedirs(value, exist_ok=True)


if __name__ == "__main__":
    arg_parser = __init_arg_parser()
    args = arg_parser.parse_args()

    labeler = ImageLabeler()

    assert os.path.isdir(args.source_directory), f'Directory "{args.source_directory} does not exist"'

    __create_if_not_exist_directories(LABEL_CLASSES_DIRECTORIES)

    labeler.show(src=args.source_directory,
                 label_classes_dict=LABEL_CLASSES_DIRECTORIES)
