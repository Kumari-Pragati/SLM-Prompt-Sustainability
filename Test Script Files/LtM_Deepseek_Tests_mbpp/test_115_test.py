import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_list_with_elements(self):
        self.assertFalse(empty_dit([{'a': 1}, {'b': 2}]))

    def test_list_with_empty_dictionaries(self):
        self.assertTrue(empty_dit([{}, {}]))

    def test_list_with_non_empty_and_empty_dictionaries(self):
        self.assertFalse(empty_dit([{'a': 1}, {}]))

    def test_single_empty_dictionary(self):
        self.assertTrue(empty_dit([{}]))

    def test_single_non_empty_dictionary(self):
        self.assertFalse(empty_dit([{'a': 1}]))
