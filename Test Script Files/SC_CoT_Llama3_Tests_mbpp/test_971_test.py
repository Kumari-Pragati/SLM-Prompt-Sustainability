import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(maximum_segments(10, 2, 3, 5), 4)

    def test_edge_case_n_zero(self):
        self.assertEqual(maximum_segments(0, 2, 3, 5), 0)

    def test_edge_case_n_one(self):
        self.assertEqual(maximum_segments(1, 2, 3, 5), 1)

    def test_edge_case_a_zero(self):
        self.assertEqual(maximum_segments(10, 0, 3, 5), 1)

    def test_edge_case_b_zero(self):
        self.assertEqual(maximum_segments(10, 2, 0, 5), 1)

    def test_edge_case_c_zero(self):
        self.assertEqual(maximum_segments(10, 2, 3, 0), 1)

    def test_edge_case_a_b_c_zero(self):
        self.assertEqual(maximum_segments(10, 0, 0, 0), 1)

    def test_invalid_input_n_negative(self):
        with self.assertRaises(IndexError):
            maximum_segments(-1, 2, 3, 5)

    def test_invalid_input_a_negative(self):
        with self.assertRaises(IndexError):
            maximum_segments(10, -1, 3, 5)

    def test_invalid_input_b_negative(self):
        with self.assertRaises(IndexError):
            maximum_segments(10, 2, -1, 5)

    def test_invalid_input_c_negative(self):
        with self.assertRaises(IndexError):
            maximum_segments(10, 2, 3, -1)
