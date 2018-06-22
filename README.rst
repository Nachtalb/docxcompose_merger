==================
Docxcompose Merger
==================

This is a simple script to auto merge ``.docx`` Word files, via `docxcompose <https://pypi.org/project/docxcompose/>`_

.. contents:: Table of Contents


Installation
------------

Clone the repository

    $ git clone https://github.com/Nachtalb/docxcompose_merger.git

Install install requirements

    $ pip install -r requirements.txt


Usage
-----

Put your Word files in the ``templates`` folder and run the build.py script:

    $ python build.py

Find your generated files in the ``export`` folder.

If you don't want to use these folders you can use the following arguments:

    usage: Docxcompose Auto File Merger [-h] [-d [D]] [-o [O]]

    optional arguments:
      -h, --help  show this help message and exit
      -d [D]      Folder with docx files to merge. Files are sorted by name, like
                  this the first onewill be the master file.
      -o [O]      Output directory or output filename


References
----------

  * Github: https://github.com/Nachtalb/docxcompose_merger
  * Docxcompose: https://pypi.org/project/docxcompose/


Copyright & License
-------------------

Copyright (c) 2018, `Nick Espig <https://github.com/Nachtalb/>`_. MIT License.
