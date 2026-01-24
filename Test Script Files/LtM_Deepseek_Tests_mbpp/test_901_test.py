import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(smallest_multiple(1), 1)
        self.assertEqual(smallest_multiple(2), 2)

    def test_edge_conditions(self):
        self.assertEqual(smallest_multiple(0), None)
        self.assertEqual(smallest_multiple(-1), None)

    def test_boundary_conditions(self):
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 30)

    def test_complex_cases(self):
        self.assertEqual(smallest_multiple(10), 2520)
        self.assertEqual(smallest_multiple(15), 360360)
