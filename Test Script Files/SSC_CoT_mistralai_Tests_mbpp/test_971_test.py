import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(maximum_segments(3, 1, 2, 3), 3)
        self.assertEqual(maximum_segments(5, 1, 2, 3), 5)
        self.assertEqual(maximum_segments(7, 1, 2, 3), 7)

    def test_edge_cases(self):
        self.assertEqual(maximum_segments(0, 1, 2, 3), 0)
        self.assertEqual(maximum_segments(1, 1, 2, 3), 1)
        self.assertEqual(maximum_segments(2, 1, 2, 3), 2)
        self.assertEqual(maximum_segments(3, 1, 2, 3), 3)
        self.assertEqual(maximum_segments(4, 1, 2, 3), 4)

    def test_boundary_conditions(self):
        self.assertEqual(maximum_segments(9, 1, 2, 3), 9)
        self.assertEqual(maximum_segments(10, 1, 2, 3), 10)
        self.assertEqual(maximum_segments(11, 1, 2, 3), 11)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            maximum_segments(-1, 1, 2, 3)
        with self.assertRaises(ValueError):
            maximum_segments(0, 0, 2, 3)
        with self.assertRaises(ValueError):
            maximum_segments(1, -1, 2, 3)
        with self.assertRaises(ValueError):
            maximum_segments(1, 1, 0, 3)
        with self.assertRaises(ValueError):
            maximum_segments(1, 1, 2, 0)
