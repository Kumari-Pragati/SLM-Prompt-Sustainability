import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_tuples([], 5), '[]')

    def test_single_tuple(self):
        self.assertEqual(find_tuples([(1, 2, 3)], 5), '[]')

    def test_multiple_tuples(self):
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6)], 5), '[[(4, 5, 6)]]')

    def test_multiple_tuples_with_no_matches(self):
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 7)], 5), '[]')

    def test_multiple_tuples_with_some_matches(self):
        self.assertEqual(find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 5), '[[(4, 5, 6)]]')

    def test_k_is_zero(self):
        with self.assertRaises(TypeError):
            find_tuples([(1, 2, 3)], 0)

    def test_k_is_negative(self):
        with self.assertRaises(TypeError):
            find_tuples([(1, 2, 3)], -5)
