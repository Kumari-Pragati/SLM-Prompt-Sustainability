import unittest
from mbpp_970_code import min_of_two

class TestMinOfTwo(unittest.TestCase):

    # Simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(min_of_two(3, 5), 3)
        self.assertEqual(min_of_two(7, 2), 2)
        self.assertEqual(min_of_two(0, 0), 0)

    # Edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(min_of_two(0, 1), 0)
        self.assertEqual(min_of_two(-1, 0), -1)
        self.assertEqual(min_of_two(-1, -2), -2)
        self.assertEqual(min_of_two(float('-inf'), float('inf')), float('-inf'))

    # More complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(min_of_two(float('nan'), 1), float('nan'))
        self.assertEqual(min_of_two(float('inf'), float('-inf')), float('-inf'))
        self.assertEqual(min_of_two(1, 1), 1)
