import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_tuple((1, 2, 2, 3, 3)), (1, 2, 3))

    def test_empty_input(self):
        self.assertEqual(remove_tuple(()), ())

    def test_single_input(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_duplicate_input(self):
        self.assertEqual(remove_tuple((1, 1, 2)), (1, 2))

    def test_min_max_values(self):
        self.assertEqual(remove_tuple((-1000000, -1, 0, 1, 1000000)), (-1000000, -1, 0, 1, 1000000))

    def test_large_input(self):
        large_input = tuple(range(1000000))
        self.assertEqual(len(remove_tuple(large_input)), len(set(large_input)))
