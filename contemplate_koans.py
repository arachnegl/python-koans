#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Acknowledgment:
#
# Python Koans is a port of Ruby Koans originally written by Jim Weirich
# and Joe O'brien of Edgecase. There are some differences and tweaks specific
# to the Python language, but a great deal of it has been copied wholesale.
# So thanks guys!
#

import sys

if __name__ == '__main__':
    if sys.version_info < (3, 3):

        print(
            "\n********************************************************\n"
            "WARNING:\n"
            "Python Koans was designed for Python 3.3 or greater.\n"
            "Your version of Python is older, lets see how far we get...\n"
            "********************************************************\n"
        )

    from runner.mountain import Mountain

    Mountain().walk_the_path(sys.argv)
