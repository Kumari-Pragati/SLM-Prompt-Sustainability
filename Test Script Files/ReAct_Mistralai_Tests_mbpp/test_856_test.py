import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(find_Min_Swaps([], 0), 0)

    def test_single_element_array(self):
        for element in [0, 1]:
            self.assertEqual(find_Min_Swaps([element], 1), 0 if element == 0 else 1)

    def test_all_zeros(self):
        self.assertEqual(find_Min_Swaps([0] * 5, 5), 5)

    def test_all_ones(self):
        self.assertEqual(find_Min_Swaps([1] * 5, 5), 0)

    def test_mixed_array_1(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 0], 5), 3)

    def test_mixed_array_2(self):
        self.assertEqual(find_Min_Swaps([1, 0, 1, 0, 1, 0, 1], 7), 4)

    def test_mixed_array_3(self):
        self.assertEqual(find_Min_Swaps([1, 0, 1, 0, 1, 0, 1, 0], 8), 5)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            find_Min_Swaps([0, 1], -1)

    def test_array_length_zero(self):
        with self.assertRaises(ValueError):
            find_Min_Swaps([], 0)
