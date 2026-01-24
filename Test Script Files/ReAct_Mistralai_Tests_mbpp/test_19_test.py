import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(test_duplicate([]))

    def test_single_element(self):
        self.assertFalse(test_duplicate([1]))

    def test_duplicate_single_element(self):
        self.assertTrue(test_duplicate([1, 1]))

    def test_unique_elements(self):
        self.assertFalse(test_duplicate([1, 2, 3]))

    def test_duplicate_elements_different_order(self):
        self.assertTrue(test_duplicate([1, 2, 2, 3]))

    def test_duplicate_elements_same_order(self):
        self.assertTrue(test_duplicate([1, 1, 2, 3]))

    def test_negative_numbers(self):
        self.assertTrue(test_duplicate([-1, -2, -3]))

    def test_positive_and_negative_numbers(self):
        self.assertTrue(test_duplicate([1, -2, 3]))

    def test_mixed_data_types(self):
        self.assertRaises(TypeError, test_duplicate, [1, 'a', 2])
