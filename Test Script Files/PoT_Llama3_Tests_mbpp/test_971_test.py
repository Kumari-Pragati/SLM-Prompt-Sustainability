import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_segments(5, 2, 3, 1), 2)

    def test_edge_case_a(self):
        self.assertEqual(maximum_segments(10, 2, 3, 1), 2)

    def test_edge_case_b(self):
        self.assertEqual(maximum_segments(10, 2, 3, 4), 2)

    def test_edge_case_c(self):
        self.assertEqual(maximum_segments(10, 2, 3, 5), 2)

    def test_edge_case_a_b(self):
        self.assertEqual(maximum_segments(10, 2, 3, 2), 2)

    def test_edge_case_a_c(self):
        self.assertEqual(maximum_segments(10, 2, 3, 3), 2)

    def test_edge_case_b_c(self):
        self.assertEqual(maximum_segments(10, 2, 3, 4), 2)

    def test_edge_case_a_b_c(self):
        self.assertEqual(maximum_segments(10, 2, 3, 5), 2)

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            maximum_segments(-1, 2, 3, 1)

    def test_invalid_input2(self):
        with self.assertRaises(IndexError):
            maximum_segments(5, -2, 3, 1)

    def test_invalid_input3(self):
        with self.assertRaises(IndexError):
            maximum_segments(5, 2, -3, 1)

    def test_invalid_input4(self):
        with self.assertRaises(IndexError):
            maximum_segments(5, 2, 3, -1)
