#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = False


class AboutAsserts(unittest.TestCase):

    def test_assert_truth(self):

        assert False # replace with True

    def test_equality(self):

        assert __ == 1 + 1

    def test_equality_with_assignment(self):

        expected_value = __
        actual_value = 1 + 1

        assert expected_value == actual_value
