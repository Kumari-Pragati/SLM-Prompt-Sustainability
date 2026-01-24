import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_tuples([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), '[[3, 6, 9]]')

    def test_edge_case(self):
        self.assertEqual(find_tuples([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]')

    def test_edge_case2(self):
        self.assertEqual(find_tuples([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10), '[]')

    def test_corner_case(self):
        self.assertEqual(find_tuples([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), '[]')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_tuples(None, 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            find_tuples([1, 2, 3], None)
