import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):
    def test_add_tuple(self):
        self.assertEqual(add_tuple([1, 2, 3], (4, 5, 6)), [1, 2, 3, 4, 5, 6])
        self.assertEqual(add_tuple([1, 2, 3], (4, 5)), [1, 2, 3, 4, 5])
        self.assertEqual(add_tuple([1, 2, 3], (4,)), [1, 2, 3, 4])
        self.assertEqual(add_tuple([1, 2, 3], ()), [1, 2, 3])
        self.assertEqual(add_tuple([], (4, 5, 6)), [4, 5, 6])
        self.assertEqual(add_tuple([], (4, 5)), [4, 5])
        self.assertEqual(add_tuple([], (4,)), [4])
        self.assertEqual(add_tuple([], ()), [])
