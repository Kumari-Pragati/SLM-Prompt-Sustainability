import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):
    def test_empty_lists(self):
        self.assertTrue(same_order([], []))

    def test_single_element_lists(self):
        self.assertTrue(same_order([1], [1]))
        self.assertFalse(same_order([1], [2]))

    def test_common_elements(self):
        self.assertTrue(same_order([1, 2, 3], [2, 3, 1]))
        self.assertTrue(same_order([1, 2, 2, 3], [2, 2, 1, 3]))

    def test_dissimilar_lists(self):
        self.assertFalse(same_order([1, 2, 3], [4, 5, 6]))

    def test_lists_with_duplicates(self):
        self.assertTrue(same_order([1, 2, 2, 3, 3], [2, 2, 3, 3, 1]))
