import unittest
from mbpp_225_code import find_Min

class TestFind_Min(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 4), 4)

    def test_edge_low(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 0), 1)

    def test_edge_high(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 4), 4)

    def test_edge_equal(self):
        self.assertEqual(find_Min([1, 1, 1, 1, 1], 0, 4), 1)

    def test_edge_low_equal(self):
        self.assertEqual(find_Min([1, 1, 1, 1, 1], 0, 0), 1)

    def test_edge_high_equal(self):
        self.assertEqual(find_Min([1, 1, 1, 1, 1], 0, 4), 1)

    def test_edge_low_high_equal(self):
        self.assertEqual(find_Min([1, 1, 1, 1, 1], 0, 0), 1)

    def test_edge_low_high(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 0, 1), 1)

    def test_edge_high_low(self):
        self.assertEqual(find_Min([1, 2, 3, 4, 5], 4, 4), 4)

    def test_edge_low_high_equal(self):
        self.assertEqual(find_Min([1, 1, 1, 1, 1], 0, 4), 1)

    def test_edge_high_low_equal(self):
        self.assertEqual(find_Min([1, 1, 1, 1, 1], 4, 0), 1)
