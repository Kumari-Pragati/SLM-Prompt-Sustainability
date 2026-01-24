import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_odd([1, 3, 5]), 3)
        self.assertEqual(count_odd([2, 4, 6]), 0)
        self.assertEqual(count_odd([1, 2, 3]), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_odd([]), 0)
        self.assertEqual(count_odd([0]), 0)
        self.assertEqual(count_odd([1]), 1)
        self.assertEqual(count_odd([-1]), 1)
        self.assertEqual(count_odd([2147483647]), 1)
        self.assertEqual(count_odd([-2147483648]), 1)

    def test_complex_scenarios(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)
        self.assertEqual(count_odd([-1, -2, -3, -4, -5, -6, -7, -8, -9]), 9)
        self.assertEqual(count_odd([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)
        self.assertEqual(count_odd([-0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 5)
