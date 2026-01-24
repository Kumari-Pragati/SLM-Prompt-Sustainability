import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(find_Odd_Pair([1, 1, 2, 3, 4], 5), 1)
        self.assertEqual(find_Odd_Pair([4, 4, 4, 5, 4], 5), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)
        self.assertEqual(find_Odd_Pair([1], 1), 0)
        self.assertEqual(find_Odd_Pair([1, 1], 2), 0)
        self.assertEqual(find_Odd_Pair([1, 1, 1], 3), 0)
        self.assertEqual(find_Odd_Pair([1, 1, 1, 1], 4), 0)
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6], 6), 3)
        self.assertEqual(find_Odd_Pair([1, 1, 2, 3, 4, 5], 6), 1)

    def test_special_cases(self):
        self.assertEqual(find_Odd_Pair([0, 1, 2], 3), 1)
        self.assertEqual(find_Odd_Pair([1, 3, 5], 3), 1)
        self.assertEqual(find_Odd_Pair([2, 4, 6], 3), 0)
