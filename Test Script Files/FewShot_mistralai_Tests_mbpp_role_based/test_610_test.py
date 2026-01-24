import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertRaises(IndexError, remove_kth_element, [], 0)

    def test_single_element(self):
        self.assertEqual(remove_kth_element([1], 0), [])
        self.assertEqual(remove_kth_element([1], 1), [])

    def test_kth_equal_to_length(self):
        self.assertRaises(IndexError, remove_kth_element, [1, 2, 3], 3)

    def test_kth_greater_than_length(self):
        self.assertRaises(IndexError, remove_kth_element, [1, 2, 3], 4)

    def test_kth_less_than_zero(self):
        self.assertRaises(IndexError, remove_kth_element, [1, 2, 3], -1)

    def test_typical_use_case(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4], 2), [1, 2, 4])
