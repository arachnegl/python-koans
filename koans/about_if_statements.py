#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = None


class AboutIfStatements(unittest.TestCase):

    def test_if_statement_one(self):

        result = 'original'

        if True:
            result = 'updated'

        assert __ == result

    def test_if_statement_two(self):

        result = 'original'

        if False:
            result = 'updated'

        assert __ == result

    def test_if_else_one(self):

        result = 'original'

        if True:
            result = 'updated by True branch'
        else:
            result = 'updated by False branch'

        assert __ == result

    def test_if_else_two(self):

        result = 'original'

        if False:
            result = 'updated by True branch'
        else:
            result = 'updated by False branch'

        assert __ == result

    def test_if_then_elif_else(self):

        vowels = 'aeiou'

        letter = 'f'

        if letter in vowels:
            result = 'is vowel'
        else:
            result = 'not vowel'

        assert __ == result
