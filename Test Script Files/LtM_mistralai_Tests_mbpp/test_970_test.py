import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_of_two(1, 2), 1)
        self.assertEqual(min_of_two(2, 1), 1)
        self.assertEqual(min_of_two(0, 1), 0)
        self.assertEqual(min_of_two(1, 0), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_of_two(-1, 0), -1)
        self.assertEqual(min_of_two(0, -1), -1)
        self.assertEqual(min_of_two(0, 0), 0)
        self.assertEqual(min_of_two(float('inf'), 0), 0)
        self.assertEqual(min_of_two(0, float('inf')), 0)
