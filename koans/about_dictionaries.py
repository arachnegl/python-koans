#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from runner.koan import __


class AboutDictionaries(unittest.TestCase):

    def test_creating_dictionaries(self):

        empty_dict = dict()

        self.assertEqual(dict, type(empty_dict))
        self.assertDictEqual({}, empty_dict)
        self.assertEqual(__, len(empty_dict))

    def test_dictionary_literals(self):

        empty_dict = {}

        self.assertEqual(dict, type(empty_dict))

        babel_fish = {'one': 'uno', 'two': 'dos'}

        self.assertEqual(__, len(babel_fish))

    def test_accessing_dictionaries(self):

        babel_fish = {'one': 'uno', 'two': 'dos'}

        self.assertEqual(__, babel_fish['one'])
        self.assertEqual(__, babel_fish['two'])

    def test_changing_dictionaries(self):

        babel_fish = {'one': 'uno', 'two': 'dos'}
        babel_fish['one'] = 'eins'

        expected = {'two': 'dos', 'one': __}
        self.assertDictEqual(expected, babel_fish)

    def test_dictionary_is_unordered(self):

        dict1 = {'one': 'uno', 'two': 'dos'}
        dict2 = {'two': 'dos', 'one': 'uno'}

        self.assertEqual(__, dict1 == dict2)

    def test_dictionary_keys_and_values(self):

        babel_fish = {'one': 'uno', 'two': 'dos'}

        # testing lengths
        self.assertEqual(__, len(babel_fish.keys()))
        self.assertEqual(__, len(babel_fish.values()))

        # testing membership
        self.assertEqual(__, 'one' in babel_fish.keys())
        self.assertEqual(__, 'two' in babel_fish.values())
        self.assertEqual(__, 'uno' in babel_fish.keys())
        self.assertEqual(__, 'dos' in babel_fish.values())
