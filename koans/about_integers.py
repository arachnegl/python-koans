#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = False


class AboutIntegers(unittest.TestCase):

    def test_integer_creation(self):

        an_integer = 5

        assert type(an_integer) == __

    def test_integer_constructor_useful_for_converting_from_string(self):

        five = '5'

        assert type(five) == __

        another_five = int('5')

        assert type(another_five) == __

    def test_integer_arithmetic(self):

        assert 1 + 3 == __
        assert 3 * 3 == __
        assert 3 ** 2 == __
        assert 9 / 3 == __
        assert 6 - 3 == __

    def test_integers_comparisons(self):

        assert (1 < 3)  == __         # less than
        assert (3 > 3)  == __         # more than
        assert (3 == 2) == __         # equality
        assert (9 <= 3) == __         # less or equal than
        assert (6 >= 3) == __         # more or equal than
