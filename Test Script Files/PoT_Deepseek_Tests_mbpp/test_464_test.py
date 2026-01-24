import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))

    def test_edge_case_with_empty_dict(self):
        self.assertTrue(check_value({}, 0))

    def test_boundary_case_with_single_element(self):
        self.assertTrue(check_value({'a': 1}, 1))
        self.assertFalse(check_value({'a': 1}, 0))

    def test_corner_case_with_multiple_same_values(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))
        self.assertFalse(check_value({'a': 1, 'b': 2, 'c': 1}, 1))

    def test_corner_case_with_different_keys_same_values(self):
        self.assertTrue(check_value({'a': 1, 'b': 1}, 1))
        self.assertFalse(check_value({'a': 1, 'b': 2}, 1))

    def test_corner_case_with_large_dict(self):
        self.assertTrue(check_value({'a': 1000, 'b': 1000, 'c': 1000}, 1000))
        self.assertFalse(check_value({'a': 1000, 'b': 2000, 'c': 1000}, 1000))
