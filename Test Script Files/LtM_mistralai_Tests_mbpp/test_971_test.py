import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(maximum_segments(3, 1, 1, 1), 3)
        self.assertEqual(maximum_segments(4, 1, 1, 2), 4)
        self.assertEqual(maximum_segments(5, 1, 2, 2), 5)

    def test_edge_cases(self):
        self.assertEqual(maximum_segments(0, 1, 1, 1), 0)
        self.assertEqual(maximum_segments(1, 1, 1, 1), 1)
        self.assertEqual(maximum_segments(2, 2, 1, 1), 2)
        self.assertEqual(maximum_segments(3, 3, 3, 1), 3)

    def test_boundary_conditions(self):
        self.assertEqual(maximum_segments(100000, 1, 1, 1), 100000)
        self.assertEqual(maximum_segments(100000, 1, 100000, 1), 100000)
        self.assertEqual(maximum_segments(100000, 100000, 1, 1), 100000)

    def test_combined_scenarios(self):
        self.assertEqual(maximum_segments(5, 2, 3, 4), 5)
        self.assertEqual(maximum_segments(6, 2, 3, 5), 6)
        self.assertEqual(maximum_segments(7, 3, 4, 5), 7)
