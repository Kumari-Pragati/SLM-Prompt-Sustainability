import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(closest_num(1), 0)
        self.assertEqual(closest_num(2), 1)
        self.assertEqual(closest_num(3), 2)
        self.assertEqual(closest_num(4), 3)
        self.assertEqual(closest_num(5), 4)

    def test_edge(self):
        self.assertEqual(closest_num(0), -1)
        self.assertEqual(closest_num(1), 0)
        self.assertEqual(closest_num(2), 1)
        self.assertEqual(closest_num(3), 2)
        self.assertEqual(closest_num(4), 3)
        self.assertEqual(closest_num(5), 4)

    def test_negative(self):
        self.assertEqual(closest_num(-1), -2)
        self.assertEqual(closest_num(-2), -3)
        self.assertEqual(closest_num(-3), -4)
        self.assertEqual(closest_num(-4), -5)
