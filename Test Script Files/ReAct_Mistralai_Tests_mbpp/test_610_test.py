import unittest
from mbpp_610_code import range
from six.moves import xrange

from610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(IndexError, remove_kth_element, [], 1)

    def test_single_element(self):
        self.assertEqual(remove_kth_element([1], 1), [])

    def test_kth_equal_to_length(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 3), [1, 2])

    def test_kth_greater_than_length(self):
        self.assertRaises(IndexError, remove_kth_element, [1, 2, 3], 4)

    def test_kth_less_than_zero(self):
        self.assertRaises(IndexError, remove_kth_element, [1, 2, 3], -1)

    def test_kth_in_range(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 1), [3])
        self.assertEqual(remove_kth_element([1, 2, 3], 2), [1])

    def test_kth_at_beginning(self):
        self.assertEqual(remove_kth_element([3, 1, 2], 1), [3])

    def test_kth_at_end(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 3), [1, 2])

    def test_kth_in_middle(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4], 2), [1, 3, 4])

    def test_mixed_data_types(self):
        self.assertEqual(remove_kth_element([1, 2, 'a', 3], 2), [1, 'a', 3])

    def test_large_list(self):
        large_list = list(xrange(1000))
        self.assertEqual(remove_kth_element(large_list, 500), large_list[:500])
