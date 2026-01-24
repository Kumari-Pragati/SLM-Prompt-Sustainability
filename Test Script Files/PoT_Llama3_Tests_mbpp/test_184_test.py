import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 3))

    def test_edge_case_equal(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 5))

    def test_edge_case_greater(self):
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 6))

    def test_edge_case_empty_list(self):
        self.assertFalse(greater_specificnum([], 5))

    def test_edge_case_single_element(self):
        self.assertFalse(greater_specificnum([1], 5))

    def test_edge_case_num_is_zero(self):
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 0))

    def test_edge_case_num_is_negative(self):
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], -1))
