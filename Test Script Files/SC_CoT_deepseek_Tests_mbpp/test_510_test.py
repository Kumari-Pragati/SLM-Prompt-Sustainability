import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 4)

    def test_edge_case(self):
        self.assertEqual(no_of_subsequences([], 0), 1)
        self.assertEqual(no_of_subsequences([1, 2, 3], 0), 0)

    def test_corner_case(self):
        self.assertEqual(no_of_subsequences([1, 1, 1], 1), 7)
        self.assertEqual(no_of_subsequences([1, 2, 3], 1), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            no_of_subsequences("1, 2, 3", 3)
        with self.assertRaises(TypeError):
            no_of_subsequences([1, 2, "3"], 3)
        with self.assertRaises(TypeError):
            no_of_subsequences([1, 2, 3], "3")
