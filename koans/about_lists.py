#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = False


class AboutLists(unittest.TestCase):

    def test_creating_lists(self):

        empty_list = list()

        assert list == type(empty_list)
        assert __ == len(empty_list)

    def test_list_literals(self):

        nums = list()
        assert [] == nums

        nums[0:] = [1]
        assert [1] ==  nums

        nums[1:] = [2]
        assert [1, __] == nums

        nums.append(333)
        assert [1, 2, __] == nums

    def test_accessing_list_elements(self):

        noms = ['peanut', 'butter', 'and', 'jelly']

        assert __ == noms[0]
        assert __ == noms[3]
        assert __ == noms[-1]
        assert __ == noms[-3]

    def test_slicing_lists(self):

        noms = ['peanut', 'butter', 'and', 'jelly']

        assert __ == noms[0:1]
        assert __ == noms[0:2]
        assert __ == noms[2:2]
        assert __ == noms[2:20]
        assert __ == noms[4:0]
        assert __ == noms[4:100]
        assert __ == noms[5:0]

    def test_slicing_to_the_edge(self):

        noms = ['peanut', 'butter', 'and', 'jelly']

        assert __ == noms[2:]
        assert __ == noms[:2]

    def test_lists_and_ranges(self):

        assert range == type(range(5))
        assert not [1, 2, 3, 4, 5] == range(1, 6)
        assert __ == list(range(5))
        assert __ == list(range(5, 9))

    def test_ranges_with_steps(self):

        assert __ == list(range(0, 8, 2))
        assert __ == list(range(1, 8, 3))
        assert __ == list(range(5, -7, -4))
        assert __ == list(range(5, -8, -4))

    def test_insertions(self):

        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        assert __ == knight

        knight.insert(0, 'Arthur')
        assert __ == knight

    def test_popping_lists(self):

        stack = [10, 20, 30, 40]
        stack.append('last')

        assert __ == stack

        popped_value = stack.pop()
        assert __ == popped_value
        assert __ == stack

        popped_value = stack.pop(1)
        assert __ == popped_value
        assert __ == stack

    def test_making_queues(self):

        queue = [1, 2]
        queue.append('last')

        assert __ == queue

        popped_value = queue.pop(0)
        assert __ == popped_value
        assert __ == queue
