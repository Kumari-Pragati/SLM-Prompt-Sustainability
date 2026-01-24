import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(maximum_segments(5, 1, 2, 1), 3)
        self.assertEqual(maximum_segments(10, 2, 3, 4), 4)

    def test_boundary_conditions(self):
        self.assertEqual(maximum_segments(0, 1, 2, 3), 0)
        self.assertEqual(maximum_segments(100, 100, 100, 100), 1)

    def test_edge_conditions(self):
        self.assertEqual(maximum_segments(15, 5, 5, 5), 3)
        self.assertEqual(maximum_segments(20, 10, 10, 10), 3)

    def test_complex_cases(self):
        self.assertEqual(maximum_segments(25, 5, 6, 7), 4)
        self.assertEqual(maximum_segments(30, 10, 11, 12), 4)
