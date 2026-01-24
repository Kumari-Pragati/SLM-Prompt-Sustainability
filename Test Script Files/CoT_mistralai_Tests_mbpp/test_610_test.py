import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(IndexError, remove_kth_element, [], 0)
        self.assertRaises(IndexError, remove_kth_element, [], 1)

    def test_single_element(self):
        self.assertEqual(remove_kth_element([1], 0), [])
        self.assertEqual(remove_kth_element([1], 1), [])

    def test_typical_case(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 2), [1, 2, 4, 5])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 0), [2, 3, 4, 5])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 4), [1, 2, 3])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])

    def test_negative_index(self):
        self.assertRaises(IndexError, remove_kth_element, [1, 2, 3], -1)
        self.assertRaises(IndexError, remove_kth_element, [1, 2, 3], -2)

    def test_index_larger_than_list_length(self):
        self.assertRaises(IndexError, remove_kth_element, [1, 2, 3], 4)
