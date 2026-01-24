import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 1, 0], 6), 1)

    def test_all_zeros(self):
        self.assertEqual(find_Min_Swaps([0, 0, 0, 0], 4), 0)

    def test_all_ones(self):
        self.assertEqual(find_Min_Swaps([1, 1, 1, 1], 4), 0)

    def test_mixed_ones_and_zeros(self):
        self.assertEqual(find_Min_Swaps([0, 1, 1, 0, 1, 0], 6), 1)

    def test_empty_array(self):
        self.assertEqual(find_Min_Swaps([], 0), 0)

    def test_single_element(self):
        self.assertEqual(find_Min_Swaps([0], 1), 0)

    def test_single_zero(self):
        self.assertEqual(find_Min_Swaps([1], 1), 0)

    def test_single_one(self):
        self.assertEqual(find_Min_Swaps([0], 1), 0)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            find_Min_Swaps([-1, 0, 1, 0], 4)

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            find_Min_Swaps([0.5, 1, 0, 1], 4)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            find_Min_Swaps(12345, 5)
