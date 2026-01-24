import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):

    def test_odd_pair_exists(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 6)

    def test_odd_pair_does_not_exist(self):
        self.assertEqual(find_Odd_Pair([2, 4, 6, 8, 10], 5), 0)

    def test_single_element(self):
        self.assertEqual(find_Odd_Pair([1], 1), 0)

    def test_empty_list(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_Odd_Pair([-1, -2, -3, -4, -5], 5), 10)

    def test_large_numbers(self):
        self.assertEqual(find_Odd_Pair([1000000000, 2000000000, 3000000000, 4000000000, 5000000000], 5), 10)
