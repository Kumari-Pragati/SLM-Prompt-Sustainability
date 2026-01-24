import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_non_empty_list(self):
        self.assertFalse(empty_dit([{'a': 1}]))

    def test_list_with_empty_dict(self):
        self.assertFalse(empty_dit([{}]))

    def test_list_with_non_empty_dict(self):
        self.assertFalse(empty_dit([{'a': 1, 'b': 2}]))

    def test_empty_dict_in_list(self):
        self.assertFalse(empty_dit([{}, {}]))

    def test_list_with_none(self):
        self.assertFalse(empty_dit([None]))

    def test_list_with_multiple_types(self):
        self.assertFalse(empty_dit([1, 'a', None, {}]))

    def test_empty_list_with_none(self):
        self.assertTrue(empty_dit([None, None]))

    def test_empty_list_with_empty_dict(self):
        self.assertFalse(empty_dit([{}, {}]))

    def test_empty_list_with_non_empty_dict(self):
        self.assertFalse(empty_dit([{'a': 1}, {'b': 2}]))

    def test_empty_list_with_empty_and_non_empty_dict(self):
        self.assertFalse(empty_dit([{}, {'a': 1}]))

    def test_empty_list_with_empty_and_non_empty_dict_and_none(self):
        self.assertFalse(empty_dit([{}, {'a': 1}, None]))
