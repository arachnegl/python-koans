#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = None


class AboutControlStatements(unittest.TestCase):

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

    def test_while(self):

        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1

        assert __ == result

    def test_while_with_break(self):

        i = 1
        result = 1
        while True:
            if i > 10:
                break
            result = result * i
            i += 1

        assert __ == result

    def test_while_with_continue(self):

        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0:
                continue
            result.append(i)

        assert __ == result

    def test_for(self):

        phrase = ["fish", "and", "chips"]

        result = []
        for word in phrase:
            result.append(word.upper())

        assert [__, __, __] == result

    def test_for_with_tuples(self):

        round_table = [
            ["Lancelot", "Blue"],
            ["Galahad", "I don't know!"],
            ["Robin", "Blue! I mean Green!"],
            ["Arthur", "Is that an African Swallow or Amazonian Swallow?"],
        ]

        result = []
        for knight, answer in round_table:
            result.append("Contestant: '" + knight + "' Answer: '" + answer + "'")

        assert result[0] == __
        assert result[1] == __
        assert result[2] == __
        assert result[3] == __

    def test_for_with_conditional(self):

        pythons = [
            ("John Cleese", 1939),
            ("Terry Gilliam", 1940),
            ("Eric Idle", 1943),
            ("Michael Palin", 1943),
        ]

        born_after_1941 = []
        for comedian, age in pythons:
            if age > 1941:
                born_after_1941.append(comedian)

        assert born_after_1941 == __
