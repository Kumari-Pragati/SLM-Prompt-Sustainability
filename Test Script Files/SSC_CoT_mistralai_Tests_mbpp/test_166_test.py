import unittest
from mbpp_166_code import find_even_Pair

class TestFindEvenPair(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_even_Pair([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(find_even_Pair([2, 2, 2, 3, 4], 5), 2)
        self.assertEqual(find_even_Pair([0, 1, 2, 3, 4], 5), 2)

    def test_edge_cases(self):
        self.assertEqual(find_even_Pair([1, 2, 3], 3), 0)
        self.assertEqual(find_even_Pair([2, 2, 2], 3), 1)
        self.assertEqual(find_even_Pair([0, 0, 0], 3), 1)
        self.assertEqual(find_even_Pair([1, 2, 3], 4), 0)
        self.assertEqual(find_even_Pair([2, 2, 2], 4), 1)
        self.assertEqual(find_even_Pair([0, 0, 0], 4), 1)

    def test_boundary_conditions(self):
        self.assertEqual(find_even_Pair([1, 2, 3], 0), 0)
        self.assertEqual(find_even_Pair([2, 2, 2], 0), 0)
        self.assertEqual(find_even_Pair([0, 0, 0], 0), 0)
        self.assertEqual(find_even_Pair([1, 2, 3], 1), 0)
        self.assertEqual(find_even_Pair([2, 2, 2], 1), 0)
        self.assertEqual(find_even_Pair([0, 0, 0], 1), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_even_Pair, [1, 2, 3], 'N')
        self.assertRaises(TypeError, find_even_Pair, [1, 2, 3], 0.5)
        self.assertRaises(TypeError, find_even_Pair, [1, 2, 3], -1)
