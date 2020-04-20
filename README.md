# ImageLabeler

GUI tool to label images. Labels are appended at the front of the image filename. The images are taken from a source directory and the labeled images are placed in the destination directory.

![ImageLabeler Screenshot](https://i.imgur.com/p1tB2LK.jpg)

## Dependencies

* [PyQT5](https://pypi.org/project/PyQt5/ )

```sh
$ pip install PyQt5
```

## Usage

> Use python>=3.6

### Configure

`LABEL_CLASSES` in [ImageLabeler.py](./ImageLabeler.py) can be updated to configure the labeler.
This is a `list`, with class names. The positions of the class names matter, as the buttons and labels will follow this positioning.

### Run 

```bash
usage: ImageLabeler.py [-h] [-b BACKUP_DIRECTORY]
                       source_directory destination_directory

Run this app to label images by appending the label at the front of the
filename.

positional arguments:
  source_directory      Directory from where images will we be
                        taken.Subdirectories included.
  destination_directory
                        Directory where labeled images will be stored.

optional arguments:
  -h, --help            show this help message and exit
  -b BACKUP_DIRECTORY, --backup-directory BACKUP_DIRECTORY
                        Directory to store images that were left unlabeled.
                        Leaving this option willadd a label to the image as
                        per the label formatter used in code.

```

**Example**

```bash
$ python ImageLabeler.py src_dir des_dir -b unlabeled_dir
```

## Demo

Clone the repo. Run the demo using the following command. 

```bash
$ python ImageLabeler.py ./Demo/unsorted ./Demo/sorted -b ./Demo/unlabeled
```

## LabelFormatter
You can define your own `LabelFormatter`. Check out [LabelUtilities.py](./LabelUtilities.py).
