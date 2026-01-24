import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(find_Min_Swaps([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(find_Min_Swaps([0], 1), 0)
        self.assertEqual(find_Min_Swaps([1], 1), 0)

    def test_all_zeros_array(self):
        self.assertEqual(find_Min_Swaps([0] * 5, 5), 5)

    def test_all_ones_array(self):
        self.assertEqual(find_Min_Swaps([1] * 5, 5), 0)

    def test_mixed_array_with_zero_at_beginning(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 1], 5), 2)

    def test_mixed_array_with_zero_at_end(self):
        self.assertEqual(find_Min_Swaps([1, 0, 1, 0, 1], 5), 2)

    def test_mixed_array_with_zero_in_middle(self):
        self.assertEqual(find_Min_Swaps([1, 0, 1, 0, 1, 1], 6), 3)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            find_Min_Swaps([1, 0, 1], -1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_Min_Swaps([1, 0, 1], 3.5)
