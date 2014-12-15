#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The path to enlightenment starts with the following:

import unittest

from koans.about_asserts import AboutAsserts
from koans.about_strings import AboutStrings
#from koans.about_string_manipulation import AboutStringManipulation
#from koans.about_none import AboutNone
from koans.about_lists import AboutLists
from koans.about_dictionaries import AboutDictionaries
#from koans.about_tuples import AboutTuples
#from koans.about_methods import AboutMethods
# from koans.about_conditionals import AboutConditionalStatements
#from koans.about_true_and_false import OnTruthAndFalseness
from koans.about_loops import AboutLoopStatements
#from koans.about_sets import AboutSets
#from koans.about_triangle_project import AboutTriangleProject
#from koans.about_exceptions import AboutExceptions
#from koans.about_triangle_project2 import AboutTriangleProject2
#from koans.about_iteration import AboutIteration
#from koans.about_comprehension import AboutComprehension
#from koans.about_generators import AboutGenerators
#from koans.about_scoring_project import AboutScoringProject
#from koans.about_classes import AboutClasses
#from koans.about_with_statements import AboutWithStatements
#from koans.about_monkey_patching import AboutMonkeyPatching
#from koans.about_dice_project import AboutDiceProject
#from koans.about_method_bindings import AboutMethodBindings
#from koans.about_inheritance import AboutInheritance
#from koans.about_scope import AboutScope
#from koans.about_modules import AboutModules
#from koans.about_packages import AboutPackages
#from koans.about_class_attributes import AboutClassAttributes
#from koans.about_attribute_access import AboutAttributeAccess
#from koans.about_deleting_objects import AboutDeletingObjects
#from koans.about_proxy_object_project import *
#from koans.about_extra_credit import AboutExtraCredit


def koans():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None

    koans = [
        AboutAsserts,
        AboutStrings,
        AboutLists,
        AboutDictionaries,
        AboutLoopStatements,
    ]

    for koan in koans:
        suite.addTests(loader.loadTestsFromTestCase(koan))

    return suite
