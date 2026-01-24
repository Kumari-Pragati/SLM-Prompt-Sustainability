import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(find_Min_Swaps([], 0), 0)

    def test_all_zeros(self):
        self.assertEqual(find_Min_Swaps([0] * 5, 5), 5)

    def test_all_ones(self):
        self.assertEqual(find_Min_Swaps([1] * 5, 5), 0)

    def test_mixed_array(self):
        self.assertEqual(find_Min_Swaps([0, 1, 0, 1, 0, 1], 6), 3)

    def test_single_zero(self):
        self.assertEqual(find_Min_Swaps([1] * 5 + [0], 6), 1)

    def test_single_one(self):
        self.assertEqual(find_Min_Swaps([0] * 5 + [1], 6), 5)
