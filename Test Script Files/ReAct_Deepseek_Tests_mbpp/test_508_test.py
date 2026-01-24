import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(same_order([1, 2, 3], [2, 3, 4]))

    def test_empty_lists(self):
        self.assertTrue(same_order([], []))

    def test_no_common_elements(self):
        self.assertFalse(same_order([1, 2, 3], [4, 5, 6]))

    def test_same_elements_different_order(self):
        self.assertFalse(same_order([1, 2, 3], [3, 2, 1]))

    def test_same_elements_same_order(self):
        self.assertTrue(same_order([1, 2, 3], [1, 2, 3]))

    def test_duplicate_elements(self):
        self.assertTrue(same_order([1, 2, 2], [2, 2, 1]))

    def test_negative_numbers(self):
        self.assertTrue(same_order([-1, -2, -3], [-2, -3, -1]))

    def test_mixed_types(self):
        self.assertFalse(same_order([1, '2', 3], [1, 2, 3]))

    def test_large_lists(self):
        l1 = list(range(1, 1001))
        l2 = list(range(1000, 2001))
        self.assertFalse(same_order(l1, l2))
