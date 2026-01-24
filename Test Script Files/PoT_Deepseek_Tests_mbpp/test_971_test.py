import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_segments(10, 2, 3, 5), 4)

    def test_boundary_conditions(self):
        self.assertEqual(maximum_segments(0, 1, 1, 1), 0)
        self.assertEqual(maximum_segments(10, 0, 0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(maximum_segments(10, 10, 10, 10), 1)
        self.assertEqual(maximum_segments(15, 5, 5, 5), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            maximum_segments(-10, 2, 3, 5)
        with self.assertRaises(Exception):
            maximum_segments(10, -2, 3, 5)
        with self.assertRaises(Exception):
            maximum_segments(10, 2, -3, 5)
        with self.assertRaises(Exception):
            maximum_segments(10, 2, 3, -5)
