import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_segments(10, 2, 3, 4), 3)

    def test_boundary_conditions(self):
        self.assertEqual(maximum_segments(0, 1, 2, 3), 0)
        self.assertEqual(maximum_segments(10, 0, 0, 0), 1)

    def test_edge_cases(self):
        self.assertEqual(maximum_segments(10, 11, 12, 13), 0)
        self.assertEqual(maximum_segments(10, 1, 2, 10), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            maximum_segments("10", 2, 3, 4)
        with self.assertRaises(TypeError):
            maximum_segments(10, "2", 3, 4)
        with self.assertRaises(TypeError):
            maximum_segments(10, 2, "3", 4)
        with self.assertRaises(TypeError):
            maximum_segments(10, 2, 3, "4")
