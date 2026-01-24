import unittest
from mbpp_196_code import remove_tuples

class TestRemoveTuples(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_tuples([(1, 2), (3, 4), (5, 6)], 2), [(1, 2), (3, 4), (5, 6)])

    def test_empty_input(self):
        self.assertEqual(remove_tuples([], 2), [])

    def test_tuple_with_different_lengths(self):
        self.assertEqual(remove_tuples([(1, 2), (3, 4, 5), (6,)], 2), [ (3, 4, 5), (6,)])

    def test_tuple_with_length_equal_to_k(self):
        self.assertEqual(remove_tuples([(1, 2), (3, 4), (5, 6)], 1), [])

    def test_tuple_with_length_greater_than_k(self):
        self.assertEqual(remove_tuples([(1, 2, 3), (4, 5, 6)], 2), [(1, 2, 3), (4, 5, 6)])
