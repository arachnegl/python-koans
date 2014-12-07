#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = False


class AboutStringManipulation(unittest.TestCase):

    def test_use_format_to_interpolate_variables(self):

        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)

        assert __ == string

    def test_you_can_get_a_substring_from_a_string(self):

        string = "Bacon, lettuce and tomato"

        assert __ == string[7:10]

    def test_you_can_get_a_single_character_from_a_string(self):

        string = "Bacon, lettuce and tomato"

        assert __ == string[1]

    def test_strings_can_be_split(self):

        string = "Sausage Egg Cheese"
        words = string.split()

        assert [__, __, __] == words

    def test_strings_can_be_joined(self):

        words = ["Now", "is", "the", "time"]

        assert __ == ' '.join(words)

    def test_strings_can_change_case(self):

        assert __ == 'guido'.capitalize()
        assert __ == 'guido'.upper()
        assert __ == 'TimBot'.lower()
        assert __ == 'guido van rossum'.title()
        assert __ == 'ToTaLlY aWeSoMe'.swapcase()
