import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4], 4), 2)
        self.assertEqual(find_even_Pair([2, 4, 6, 8], 4), 6)

    def test_edge_conditions(self):
        self.assertEqual(find_even_Pair([], 0), 0)
        self.assertEqual(find_even_Pair([1], 1), 0)
        self.assertEqual(find_even_Pair([2], 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_even_Pair([0, 1], 2), 1)
        self.assertEqual(find_even_Pair([2, 3], 2), 0)
        self.assertEqual(find_even_Pair([0, 0], 2), 1)

    def test_complex_cases(self):
        self.assertEqual(find_even_Pair([1, 3, 5, 7, 9], 5), 0)
        self.assertEqual(find_even_Pair([2, 4, 6, 8, 10], 5), 10)
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5, 6], 6), 4)
