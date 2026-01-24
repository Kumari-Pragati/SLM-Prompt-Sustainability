import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):

    def test_same_order(self):
        self.assertTrue(same_order([1, 2, 3], [1, 2, 3]))
        self.assertFalse(same_order([1, 2, 3], [1, 3, 2]))
        self.assertTrue(same_order([1, 2, 3, 4], [1, 2, 3, 4]))
        self.assertFalse(same_order([1, 2, 3, 4], [1, 2, 4, 3]))
        self.assertTrue(same_order([], []))
        self.assertFalse(same_order([1, 2, 3], []))

    def test_empty_list(self):
        self.assertTrue(same_order([], []))
        self.assertFalse(same_order([1, 2, 3], []))

    def test_single_element(self):
        self.assertTrue(same_order([1], [1]))
        self.assertFalse(same_order([1], [2]))

    def test_duplicates(self):
        self.assertTrue(same_order([1, 2, 2, 3], [1, 2, 2, 3]))
        self.assertFalse(same_order([1, 2, 2, 3], [1, 2, 3, 2]))
