import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(maximum_segments(10, 2, 3, 4), 4)

    def test_boundary_conditions(self):
        self.assertEqual(maximum_segments(0, 1, 1, 1), 0)
        self.assertEqual(maximum_segments(10, 0, 0, 0), 0)

    def test_edge_conditions(self):
        self.assertEqual(maximum_segments(1, 1, 1, 1), 1)
        self.assertEqual(maximum_segments(10, 5, 5, 0), 2)
        self.assertEqual(maximum_segments(10, 0, 5, 5), 2)
        self.assertEqual(maximum_segments(10, 5, 0, 5), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            maximum_segments("10", 2, 3, 4)
        with self.assertRaises(TypeError):
            maximum_segments(10, "2", 3, 4)
        with self.assertRaises(TypeError):
            maximum_segments(10, 2, "3", 4)
        with self.assertRaises(TypeError):
            maximum_segments(10, 2, 3, "4")
