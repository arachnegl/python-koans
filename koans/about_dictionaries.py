#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

__ = None


class AboutDictionaries(unittest.TestCase):

    def test_creating_dictionaries(self):

        empty_dict = dict()

        assert dict == type(empty_dict)
        assert {} == empty_dict
        assert __ == len(empty_dict)

    def test_dictionary_literals(self):

        empty_dict = {}

        assert dict == type(empty_dict)

        babel_fish = {'one': 'uno', 'two': 'dos'}

        assert __, len(babel_fish)

    def test_accessing_dictionaries(self):

        babel_fish = {'one': 'uno', 'two': 'dos'}

        assert __ == babel_fish['one']
        assert __ == babel_fish['two']

    def test_changing_dictionaries(self):

        babel_fish = {'one': 'uno', 'two': 'dos'}
        babel_fish['one'] = 'eins'

        expected = {'two': 'dos', 'one': __}
        assert expected == babel_fish

    def test_dictionary_is_unordered(self):

        dict1 = {'one': 'uno', 'two': 'dos'}
        dict2 = {'two': 'dos', 'one': 'uno'}

        assert __ == (dict1 == dict2)

    def test_dictionary_keys_and_values(self):

        babel_fish = {'one': 'uno', 'two': 'dos'}

        # testing lengths
        assert __ == len(babel_fish.keys())
        assert __ == len(babel_fish.values())

        # testing membership
        assert __ == 'one' in babel_fish.keys()
        assert __ == 'two' in babel_fish.values()
        assert __ == 'uno' in babel_fish.keys()
        assert __ == 'dos' in babel_fish.values()
