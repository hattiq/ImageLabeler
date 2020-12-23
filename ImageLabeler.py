import argparse
import os
import sys

from PyQt5 import QtWidgets

from LabelUtilities import (LabelFormatterInterface,
                            ListPositionalLabelFormatter)
from Ui_MainWindow import Ui_MainWindow

# Positions matters
LABEL_CLASSES = ["Red", "Green", "Blue"]


class ImageLabeler:
    """
    An app that labels images by adding the label at the front of the filename.

    Images to be labeled are taken from source directory.
    labeled images are moved to the destination directory.
    """

    @staticmethod
    def show(label_classes: [str], labelFormatter: LabelFormatterInterface, src: str, des: str, bak: str = None):
        """
        Initialize and start app.

        :param src: source directory from which images are to be taken; subdirectories included.
        :param des: destination directory where labeled images are stored.
        :param bak: directory to store images that were left unlabeled. Leaving this option None will add a label to the
                    image as per the label formatter used.
        :param label_classes: A list of class names.
        :return:
        """

        app = QtWidgets.QApplication(sys.argv)
        ui = Ui_MainWindow(label_classes=label_classes,
                           src=src,
                           des=des,
                           bak=bak,
                           labelFormatter=labelFormatter)
        ui.show()
        sys.exit(app.exec_())


def __init_arg_parser() -> argparse.ArgumentParser:
    """
    Configures an ArgumentParser with arguments needed for ImageLabeler app.

    :return: A Configured argparse.ArgumentParser
    """

    parser = argparse.ArgumentParser(
        description='Run this app to label images by appending the label at the front of the filename.')

    parser.add_argument('source_directory',
                        type=str,
                        help='Directory from where images will we be taken.'
                        'Subdirectories included.')

    parser.add_argument('destination_directory',
                        type=str,
                        help='Directory where labeled images will be stored.')
    parser.add_argument('-b', '--backup-directory',
                        default=None,
                        type=str,
                        help='Directory to store images that were left unlabeled. Leaving this option will'
                             'add a label to the image as per the label formatter used in code.')

    return parser


if __name__ == "__main__":
    arg_parser = __init_arg_parser()
    args = arg_parser.parse_args()

    labeler = ImageLabeler()

    assert os.path.isdir(
        args.source_directory), f'Directory "{args.source_directory} does not exist"'

    os.makedirs(args.destination_directory, exist_ok=True)
    if args.backup_directory is not None:
        os.makedirs(args.backup_directory, exist_ok=True)

    labelFormatter = ListPositionalLabelFormatter(LABEL_CLASSES)

    labeler.show(label_classes=LABEL_CLASSES,
                 src=args.source_directory,
                 des=args.destination_directory,
                 bak=args.backup_directory,
                 labelFormatter=labelFormatter)
