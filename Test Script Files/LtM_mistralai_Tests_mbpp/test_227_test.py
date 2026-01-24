import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(3, 2, 1), 1)
        self.assertEqual(min_of_three(-1, 0, 1), -1)
        self.assertEqual(min_of_three(0, -1, 1), -1)
        self.assertEqual(min_of_three(0, 0, -1), -1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_of_three(0, 0, 0), 0)
        self.assertEqual(min_of_three(float('inf'), 0, -1), 0)
        self.assertEqual(min_of_three(-1, float('inf'), 0), -1)
        self.assertEqual(min_of_three(None, 0, 1), 0)
        self.assertEqual(min_of_three(0, None, 1), 0)
        self.assertEqual(min_of_three(0, 0, None), 0)
