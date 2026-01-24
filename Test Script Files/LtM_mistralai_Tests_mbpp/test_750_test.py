import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(add_tuple([1, 2, 3], (4, 5)), [1, 2, 3, 4, 5])
        self.assertEqual(add_tuple(["a", "b", "c"], ("d", "e", "f")), ["a", "b", "c", "d", "e", "f"])

    def test_empty_inputs(self):
        self.assertEqual(add_tuple([], ()), [])
        self.assertEqual(add_tuple((), (1, 2, 3)), (1, 2, 3))

    def test_single_input(self):
        self.assertEqual(add_tuple([1, 2, 3], (1, 2, 3)), [2, 2, 2, 3])
        self.assertEqual(add_tuple(["a", "b", "c"], ("a", "b", "c")), ["a", "b", "c", "a", "b", "c"])

    def test_edge_cases(self):
        self.assertEqual(add_tuple([0, 0, 0], (1, 2, 3)), [1, 0, 0, 2, 3])
        self.assertEqual(add_tuple(["z", "y", "x"], ("a", "b", "c")), ["z", "y", "x", "a", "b", "c"])

    def test_negative_numbers(self):
        self.assertEqual(add_tuple([1, -2, 3], (4, -5, 6)), [1, -2, 3, 4, -5, 6])
        self.assertEqual(add_tuple(["a", "b", "c"], ("d", "-e", "f")), ["a", "b", "c", "d", "-e", "f"])
