#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = False


class AboutLists(unittest.TestCase):

    def test_creating_lists(self):

        empty_list = []

        assert list == type(empty_list)
        assert __ == len(empty_list)

    def test_accessing_list_elements(self):

        noms = ['peanut', 'butter', 'and', 'jelly']

        assert __ == noms[0]
        assert __ == noms[3]

    def test_slicing_lists(self):

        noms = ['peanut', 'butter', 'and', 'jelly']

        assert __ == noms[0:1]
        assert __ == noms[0:2]
        assert __ == noms[2:]
        assert __ == noms[:2]

    def test_lists_and_ranges(self):

        assert __ == list(range(3))
        assert __ == list(range(3, 6))

    def test_insertions(self):

        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        assert __ == knight

        knight.insert(0, 'Arthur')
        assert __ == knight

    def test_popping_lists(self):

        stack = [1, 2, 3]
        stack.append('last')

        assert __ == stack

        popped_value = stack.pop()
        assert __ == popped_value
        assert __ == stack

