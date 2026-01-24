import unittest
from mbpp_115_code import empty_dit

class TestEmptyDit(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(empty_dit([{}, {}]))

    def test_empty_list(self):
        self.assertTrue(empty_dit([]))

    def test_single_empty_dict(self):
        self.assertTrue(empty_dit([{}]))

    def test_single_non_empty_dict(self):
        self.assertFalse(empty_dit([{1: 2}]))

    def test_mixed_empty_and_non_empty_dicts(self):
        self.assertFalse(empty_dit([{}, {1: 2}]))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            empty_dit('not a list')

    def test_list_with_non_dict_elements(self):
        with self.assertRaises(TypeError):
            empty_dit([1, 2, 3])
