import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_even_Pair([]), 0)

    def test_single_element(self):
        self.assertEqual(find_even_Pair([1]), 0)

    def test_even_single_pair(self):
        self.assertEqual(find_even_Pair([2, 4]), 1)

    def test_odd_single_pair(self):
        self.assertEqual(find_even_Pair([1, 3]), 0)

    def test_multiple_even_pairs(self):
        self.assertEqual(find_even_Pair([2, 4, 6, 8]), 3)

    def test_multiple_odd_pairs(self):
        self.assertEqual(find_even_Pair([1, 3, 5, 7]), 0)

    def test_mixed_pairs(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5]), 1)

    def test_boundary_case_single_pair(self):
        self.assertEqual(find_even_Pair([0, 2]), 1)

    def test_boundary_case_last_pair(self):
        self.assertEqual(find_even_Pair([2, 3]), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_even_Pair([-2, -1, 0]), 1)

    def test_large_list(self):
        large_list = [i for i in range(1000)]
        self.assertEqual(find_even_Pair(large_list), len(large_list) // 2)
