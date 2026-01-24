import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)

    def test_edge_case(self):
        self.assertEqual(get_median([1, 2, 3], [4, 5, 6], 3), 3.5)

    def test_edge_case2(self):
        self.assertEqual(get_median([1, 2, 3], [4, 5], 3), 2.5)

    def test_edge_case3(self):
        self.assertEqual(get_median([1, 2], [3, 4, 5, 6], 4), 3.5)

    def test_edge_case4(self):
        self.assertEqual(get_median([1, 3, 5], [2, 4], 3), 2.5)

    def test_invalid_input1(self):
        with self.assertRaises(IndexError):
            get_median([1, 2, 3], [4, 5], 0)

    def test_invalid_input2(self):
        with self.assertRaises(IndexError):
            get_median([1, 2, 3], [4, 5], 5)

    def test_invalid_input3(self):
        with self.assertRaises(IndexError):
            get_median([1, 2], [4, 5, 6], 5)
