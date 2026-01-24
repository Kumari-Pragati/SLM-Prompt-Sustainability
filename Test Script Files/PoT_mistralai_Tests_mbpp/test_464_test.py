import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))

    def test_edge_case_single_value(self):
        self.assertTrue(check_value({'a': 1}, 1))
        self.assertFalse(check_value({'a': 1}, 2))

    def test_edge_case_empty_dict(self):
        self.assertFalse(check_value({}, 1))

    def test_edge_case_single_key_multiple_values(self):
        self.assertFalse(check_value({'a': [1, 2]}, 1))

    def test_corner_case_mixed_types(self):
        self.assertFalse(check_value({'a': 1, 'b': '1'}, 1))
