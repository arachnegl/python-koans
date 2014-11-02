#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import Koan, __, _____


class AboutAsserts(Koan):

    def test_assert_truth(self):

        self.assertTrue(_____)  # This should be true

    def test_assert_with_message(self):

        self.assertTrue(_____, "This should be true -- Please fix this")

    def test_fill_in_values(self):

        self.assertEqual(__, 1 + 1)

    def test_assert_equality(self):

        expected_value = __
        actual_value = 1 + 1

        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):

        expected_value = __
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

    def test_unittest_asserts_work_the_same_way_as_python_asserts(self):

        # unittest is Pythons' testing framework. Google it.

        # This class called AboutAsserts inherits from Koan
        # which inherits from unittest. More on that later.

        # the .assertTrue .assertEqual methods we are calling
        # are defined within unittest.

        # The goal here is to show they work the same as the assert statement

        # To fix this test, experiement with these in the interpreter:
        # >>> assert True
        # >>> assert False

        assert False
