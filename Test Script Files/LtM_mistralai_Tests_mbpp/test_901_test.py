import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(smallest_multiple(1), 2)
        self.assertEqual(smallest_multiple(2), 2)
        self.assertEqual(smallest_multiple(3), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(smallest_multiple(0), 0)
        self.assertEqual(smallest_multiple(1000000), 2000000)
        self.assertEqual(smallest_multiple(1000001), None)

    def test_complex_and_corner_cases(self):
        self.assertEqual(smallest_multiple(4), 4)
        self.assertEqual(smallest_multiple(5), 10)
        self.assertEqual(smallest_multiple(6), 6)
        self.assertEqual(smallest_multiple(7), 14)
        self.assertEqual(smallest_multiple(8), 16)
        self.assertEqual(smallest_multiple(9), 18)
