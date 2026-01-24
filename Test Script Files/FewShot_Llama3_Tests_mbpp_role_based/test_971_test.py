import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(maximum_segments(10, 2, 3, 4), 4)

    def test_edge_case_n_zero(self):
        self.assertEqual(maximum_segments(0, 2, 3, 4), 0)

    def test_edge_case_a_zero(self):
        self.assertEqual(maximum_segments(10, 0, 3, 4), 1)

    def test_edge_case_b_zero(self):
        self.assertEqual(maximum_segments(10, 2, 0, 4), 1)

    def test_edge_case_c_zero(self):
        self.assertEqual(maximum_segments(10, 2, 3, 0), 1)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(ValueError):
            maximum_segments(-1, 2, 3, 4)

    def test_invalid_input_a_negative(self):
        with self.assertRaises(ValueError):
            maximum_segments(10, -1, 3, 4)

    def test_invalid_input_b_negative(self):
        with self.assertRaises(ValueError):
            maximum_segments(10, 2, -1, 4)

    def test_invalid_input_c_negative(self):
        with self.assertRaises(ValueError):
            maximum_segments(10, 2, 3, -1)
