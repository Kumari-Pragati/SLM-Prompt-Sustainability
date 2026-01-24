import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(maximum_segments(3, 1, 2, 3), 3)
        self.assertEqual(maximum_segments(5, 1, 2, 3), 4)
        self.assertEqual(maximum_segments(7, 1, 2, 3), 5)

    def test_edge_cases(self):
        self.assertEqual(maximum_segments(0, 1, 2, 3), 0)
        self.assertEqual(maximum_segments(1, 1, 2, 3), 1)
        self.assertEqual(maximum_segments(2, 1, 2, 3), 2)
        self.assertEqual(maximum_segments(3, 1, 2, 3), 3)
        self.assertEqual(maximum_segments(4, 1, 2, 3), 4)
        self.assertEqual(maximum_segments(5, 1, 2, 3), 4)
        self.assertEqual(maximum_segments(6, 1, 2, 3), 5)
        self.assertEqual(maximum_segments(7, 1, 2, 3), 5)
        self.assertEqual(maximum_segments(8, 1, 2, 3), 5)
        self.assertEqual(maximum_segments(9, 1, 2, 3), 6)

    def test_boundary_cases(self):
        self.assertEqual(maximum_segments(10, 1, 2, 3), 6)
        self.assertEqual(maximum_segments(10, 10, 2, 3), 10)
        self.assertEqual(maximum_segments(10, 1, 10, 3), 10)
        self.assertEqual(maximum_segments(10, 1, 2, 10), 10)
