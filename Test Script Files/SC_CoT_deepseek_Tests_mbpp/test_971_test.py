import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_segments(10, 2, 3, 4), 3)

    def test_boundary_case(self):
        self.assertEqual(maximum_segments(0, 2, 3, 4), 0)

    def test_edge_case(self):
        self.assertEqual(maximum_segments(15, 5, 10, 15), 2)
        self.assertEqual(maximum_segments(20, 10, 10, 10), 3)

    def test_corner_case(self):
        self.assertEqual(maximum_segments(2, 1, 2, 3), 1)
        self.assertEqual(maximum_segments(10, 1, 1, 1), 4)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            maximum_segments(-10, 2, 3, 4)
        with self.assertRaises(Exception):
            maximum_segments(10, -2, 3, 4)
        with self.assertRaises(Exception):
            maximum_segments(10, 2, -3, 4)
        with self.assertRaises(Exception):
            maximum_segments(10, 2, 3, -4)
