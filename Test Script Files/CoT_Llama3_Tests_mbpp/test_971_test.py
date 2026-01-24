import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(maximum_segments(10, 3, 2, 1), 4)

    def test_edge_case1(self):
        self.assertEqual(maximum_segments(1, 3, 2, 1), 1)

    def test_edge_case2(self):
        self.assertEqual(maximum_segments(2, 3, 2, 1), 2)

    def test_edge_case3(self):
        self.assertEqual(maximum_segments(3, 3, 2, 1), 3)

    def test_edge_case4(self):
        self.assertEqual(maximum_segments(4, 3, 2, 1), 4)

    def test_invalid_input1(self):
        with self.assertRaises(IndexError):
            maximum_segments(-1, 3, 2, 1)

    def test_invalid_input2(self):
        with self.assertRaises(IndexError):
            maximum_segments(10, -3, 2, 1)

    def test_invalid_input3(self):
        with self.assertRaises(IndexError):
            maximum_segments(10, 3, -2, 1)

    def test_invalid_input4(self):
        with self.assertRaises(IndexError):
            maximum_segments(10, 3, 2, -1)
