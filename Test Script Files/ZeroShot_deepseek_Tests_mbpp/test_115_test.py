import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_non_empty_list(self):
        self.assertFalse(empty_dit([{'a': 1}, {'b': 2}]))

    def test_mixed_types(self):
        self.assertFalse(empty_dit([{'a': 1}, 'b', 2]))

    def test_empty_dict(self):
        self.assertTrue(empty_dit([{}]))

    def test_none_in_list(self):
        self.assertFalse(empty_dit([None]))
