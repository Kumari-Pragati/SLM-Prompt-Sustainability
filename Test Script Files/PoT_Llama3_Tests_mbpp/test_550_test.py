import unittest
from mbpp_550_code import find_Max

class TestFindMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)

    def test_edge_case_low(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 0), 1)

    def test_edge_case_high(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)

    def test_edge_case_equal(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 0), 1)

    def test_edge_case_mid(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 1), 2)

    def test_edge_case_mid_left(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 2), 3)

    def test_edge_case_mid_right(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 1, 4), 5)

    def test_edge_case_low_high(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 4), 5)

    def test_edge_case_low_low(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 0, 0), 1)

    def test_edge_case_high_high(self):
        self.assertEqual(find_Max([1, 2, 3, 4, 5], 4, 4), 5)

    def test_edge_case_low_high_invalid(self):
        with self.assertRaises(IndexError):
            find_Max([1, 2, 3, 4, 5], 0, 5)
