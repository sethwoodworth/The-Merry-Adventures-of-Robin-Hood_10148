#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" something like:
    for line in file,
        recognize if line is a new header attribute (==)
        save that to list
        if so,
            make a new file out of that chapter
        if not,
            continue to append into the more recent chapter/section file

    then turn the list of headers into a
        book.asciidoc file that contains include::s
"""


