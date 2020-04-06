# ImageLabeler

GUI tool to copy images into specific folders. A single image is copied to all the folders you selected. The original image is deleted, but only if it was copied.

![ImageLabeler Screenshot](https://i.imgur.com/p1tB2LK.jpg)

## Dependencies

* [PyQT5](https://pypi.org/project/PyQt5/ )

```sh
$ pip install PyQt5
```

## Usage

> Use python>=3.6

### Configure

`LABEL_CLASSES_DIRECTORIES` in [ImageLabeler.py](./ImageLabeler.py) can be updated to configure the labeler.
This is a `dict`, whose keys represent labels or button text, while values are directory paths. 

### Run 

```bash
usage: ImageLabeler.py [-h] source_directory

Run this app to copy a single file into multiple folders as a labeling
technique.

positional arguments:
  source_directory  Directory from where images will we be
                    taken.Subdirectories included.

optional arguments:
  -h, --help        show this help message and exit
```

**Example**

```bash
$ python ImageLabeler.py src_dir
```

## Demo

Clone the repo. Run the demo using the following command. 

```bash
$ python ImageLabeler.py ./Demo/unsorted
```

Copied files will be stored in `./Demo/sorted/*` where `*` represents different labels.
