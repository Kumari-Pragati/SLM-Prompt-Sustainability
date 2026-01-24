import unittest
from mbpp_375_code import round_num

class TestRoundNum(unittest.TestCase):
    def test_simple_rounding(self):
        self.assertEqual(round_num(10, 2), 10)
        self.assertEqual(round_num(10, 3), 10)
        self.assertEqual(round_num(10, 4), 10)
        self.assertEqual(round_num(11, 2), 10)
        self.assertEqual(round_num(11, 3), 10)
        self.assertEqual(round_num(11, 4), 10)

    def test_edge_cases(self):
        self.assertEqual(round_num(10, 0), 10)
        self.assertEqual(round_num(10, 1), 10)
        self.assertEqual(round_num(10, 5), 10)
        self.assertEqual(round_num(10, 10), 10)
        self.assertEqual(round_num(10, 20), 10)

    def test_rounding_to_nearest(self):
        self.assertEqual(round_num(10.5, 1), 10)
        self.assertEqual(round_num(10.5, 2), 10)
        self.assertEqual(round_num(10.5, 3), 10)
        self.assertEqual(round_num(10.5, 4), 10)
        self.assertEqual(round_num(10.5, 5), 10)

    def test_rounding_to_nearest_half(self):
        self.assertEqual(round_num(10.25, 1), 10)
        self.assertEqual(round_num(10.25, 2), 10)
        self.assertEqual(round_num(10.25, 3), 10)
        self.assertEqual(round_num(10.25, 4), 10)
        self.assertEqual(round_num(10.25, 5), 10)
