import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)

    def test_single_element(self):
        for num in [1, -1]:
            self.assertEqual(find_Odd_Pair([num], 1), 0)

    def test_even_length_no_odd_pair(self):
        for even_list in [
            [2, 4, 6, 8],
            [-2, -4, -6, -8],
            [0, 0, 0, 0],
        ]:
            self.assertEqual(find_Odd_Pair(even_list, len(even_list)), 0)

    def test_even_length_with_odd_pair(self):
        for odd_list in [
            [1, 2, 4, 6],
            [-1, -2, -4, -6],
            [0, 1, 0, 2],
        ]:
            self.assertEqual(find_Odd_Pair(odd_list, len(odd_list)), 1)

    def test_odd_length_no_odd_pair(self):
        for odd_list in [
            [1, 2, 4],
            [-1, -2, -4],
            [0, 1, 0, 2, 4],
        ]:
            self.assertEqual(find_Odd_Pair(odd_list, len(odd_list)), 0)

    def test_odd_length_with_odd_pair(self):
        for odd_list in [
            [1, 2, 3],
            [-1, -2, -3],
            [0, 1, 2, 3],
            [0, 0, 1, 2],
        ]:
            self.assertEqual(find_Odd_Pair(odd_list, len(odd_list)), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_Odd_Pair([-1, 1], 2), 1)
        self.assertEqual(find_Odd_Pair([-1, -2, 1, 2], 4), 2)

    def test_zero(self):
        self.assertEqual(find_Odd_Pair([0], 1), 0)
        self.assertEqual(find_Odd_Pair([0, 0], 2), 0)
        self.assertEqual(find_Odd_Pair([0, 1, 0], 3), 1)
