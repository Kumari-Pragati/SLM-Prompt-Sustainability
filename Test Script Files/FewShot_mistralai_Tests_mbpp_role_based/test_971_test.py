import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(maximum_segments(5, 1, 2, 3), 3)

    def test_edge_case_small_n(self):
        self.assertEqual(maximum_segments(0, 1, 2, 3), 0)

    def test_edge_case_large_n(self):
        self.assertEqual(maximum_segments(100, 1, 2, 3), 100)

    def test_edge_case_negative_n(self):
        self.assertEqual(maximum_segments(-1, 1, 2, 3), -1)

    def test_edge_case_zero_a_b_c(self):
        self.assertEqual(maximum_segments(5, 0, 0, 0), 1)

    def test_edge_case_invalid_input_a(self):
        with self.assertRaises(ValueError):
            maximum_segments(5, -1, 2, 3)

    def test_edge_case_invalid_input_b(self):
        with self.assertRaises(ValueError):
            maximum_segments(5, 1, -1, 3)

    def test_edge_case_invalid_input_c(self):
        with self.assertRaises(ValueError):
            maximum_segments(5, 1, 2, -1)
