import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_non_empty_list(self):
        self.assertFalse(empty_dit([{'a': 1}]))

    def test_list_with_empty_dicts(self):
        self.assertTrue(empty_dit([{}, {}]))

    def test_list_with_non_empty_dicts(self):
        self.assertFalse(empty_dit([{'a': 1}, {'b': 2}]))

    def test_list_with_mixed_empty_and_non_empty_dicts(self):
        self.assertFalse(empty_dit([{}, {'a': 1}]))

    def test_list_with_none_elements(self):
        self.assertTrue(empty_dit([None, None]))

    def test_list_with_mixed_none_and_non_empty_dicts(self):
        self.assertFalse(empty_dit([None, {'a': 1}]))

    def test_list_with_empty_and_none_elements(self):
        self.assertTrue(empty_dit([{}, None]))

    def test_list_with_non_empty_and_none_elements(self):
        self.assertFalse(empty_dit([{'a': 1}, None]))

    def test_list_with_empty_and_non_empty_and_none_elements(self):
        self.assertFalse(empty_dit([{}, {'a': 1}, None]))
