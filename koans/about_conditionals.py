#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = None


class AboutConditionalStatements(unittest.TestCase):

    def test_if_then_else(self):

        if True:
            result = 'true value'
        else:
            result = 'false value'

        assert __ == result

    def test_if_then(self):

        result = 'default value'

        if True:
            result = 'true value'

        assert __ == result

    def test_if_then_elif_else(self):

        if False:
            result = 'first value'
        elif True:
            result = 'true value'
        else:
            result = 'default value'

        assert __ == result
