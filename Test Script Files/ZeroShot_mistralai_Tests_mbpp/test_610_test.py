import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_kth_element([], 1), [])

    def test_single_element(self):
        self.assertEqual(remove_kth_element([1], 1), [])
        self.assertEqual(remove_kth_element([1], 0), [])
        self.assertEqual(remove_kth_element([1], 2), [1])

    def test_k_greater_than_length(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 4), [1, 2, 3])

    def test_k_equal_to_length(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 3), [1, 2])

    def test_k_less_than_length(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 1), [3])
        self.assertEqual(remove_kth_element([1, 2, 3], 2), [1, 3])
