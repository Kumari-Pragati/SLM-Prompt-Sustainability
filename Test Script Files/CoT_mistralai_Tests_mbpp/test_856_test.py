import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(find_Min_Swaps([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_Min_Swaps([0], 1), 0)
        self.assertEqual(find_Min_Swaps([1], 1), 0)

    def test_all_zeros(self):
        self.assertEqual(find_Min_Swaps([0] * 5, 5), 4)

    def test_all_ones(self):
        self.assertEqual(find_Min_Swaps([1] * 5, 5), 0)

    def test_mixed_array_1(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 0], 5), 2)

    def test_mixed_array_2(self):
        self.assertEqual(find_Min_Swaps([1, 0, 1, 0, 1, 0, 1], 7), 3)

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            find_Min_Swaps([0, 1], -1)

    def test_invalid_input_array(self):
        with self.assertRaises(TypeError):
            find_Min_Swaps(123, 4)
