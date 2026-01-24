import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(clear_tuple((1, 2, 3)), ())
        self.assertEqual(clear_tuple((4,)), ())
        self.assertEqual(clear_tuple((0, 0, 0)), ())

    def test_edge_input(self):
        self.assertEqual(clear_tuple(()), ())
        self.assertEqual(clear_tuple((None,)), ())
        self.assertEqual(clear_tuple((True, False)), ())

    def test_complex_input(self):
        self.assertEqual(clear_tuple((1, 2, 3, 1, 2, 3)), ())
        self.assertEqual(clear_tuple((-10, 0, 10)), ())
        self.assertEqual(clear_tuple(('a', 'b', 'c')), ())
        self.assertEqual(clear_tuple((1.1, 2.2, 3.3)), ())
