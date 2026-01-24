import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_Position([10, 20, 30], 3, 10), 1)
        self.assertEqual(get_Position([5, 15, 25], 3, 5), 3)

    def test_edge_conditions(self):
        self.assertEqual(get_Position([0, 0, 0], 3, 1), 1)
        self.assertEqual(get_Position([10, 20, 30], 3, 1), 3)
        self.assertEqual(get_Position([], 0, 10), -1)

    def test_boundary_conditions(self):
        self.assertEqual(get_Position([10**9, 10**9, 10**9], 3, 10**9), 1)
        self.assertEqual(get_Position([1, 2, 3], 3, 1), 3)

    def test_complex_cases(self):
        self.assertEqual(get_Position([10, 20, 30], 3, 2), 2)
        self.assertEqual(get_Position([10, 20, 30], 3, 10), 1)
        self.assertEqual(get_Position([10, 20, 30], 3, 30), 3)
