import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(get_Inv_Count(arr, len(arr)), 5)

    def test_empty_list(self):
        arr = []
        self.assertEqual(get_Inv_Count(arr, len(arr)), 0)

    def test_single_element_list(self):
        arr = [1]
        self.assertEqual(get_Inv_Count(arr, len(arr)), 0)

    def test_reverse_ordered_list(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(get_Inv_Count(arr, len(arr)), 15)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(get_Inv_Count(arr, len(arr)), 15)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            get_Inv_Count(arr, -1)
