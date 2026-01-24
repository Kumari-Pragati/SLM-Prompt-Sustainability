import unittest
from mbpp_556_code import find_Odd_Pair

class TestFindOddPair(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4], 4), 2)
        self.assertEqual(find_Odd_Pair([1, 3, 5, 7], 4), 6)

    def test_edge_conditions(self):
        self.assertEqual(find_Odd_Pair([], 0), 0)
        self.assertEqual(find_Odd_Pair([1], 1), 0)
        self.assertEqual(find_Odd_Pair([2], 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_Odd_Pair([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 45)
        self.assertEqual(find_Odd_Pair([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10), 45)

    def test_complex_cases(self):
        self.assertEqual(find_Odd_Pair([1, 3, 5, 7, 9, 11], 6), 15)
        self.assertEqual(find_Odd_Pair([2, 4, 6, 8, 10, 12], 6), 0)
