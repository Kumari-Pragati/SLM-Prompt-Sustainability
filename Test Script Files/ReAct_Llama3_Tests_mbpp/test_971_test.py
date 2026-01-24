import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(maximum_segments(5, 2, 3, 4), 3)

    def test_edge_case_a(self):
        self.assertEqual(maximum_segments(1, 2, 3, 4), 0)

    def test_edge_case_b(self):
        self.assertEqual(maximum_segments(2, 2, 3, 4), 1)

    def test_edge_case_c(self):
        self.assertEqual(maximum_segments(3, 2, 3, 4), 2)

    def test_edge_case_all(self):
        self.assertEqual(maximum_segments(6, 2, 3, 4), 3)

    def test_edge_case_zero(self):
        self.assertEqual(maximum_segments(0, 2, 3, 4), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(IndexError):
            maximum_segments(-1, 2, 3, 4)

    def test_edge_case_large(self):
        self.assertEqual(maximum_segments(100, 2, 3, 4), 10)
