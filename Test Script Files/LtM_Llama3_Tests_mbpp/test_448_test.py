import unittest
from mbpp_448_code import cal_sum

class TestCalSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)
        self.assertEqual(cal_sum(3), 8)
        self.assertEqual(cal_sum(4), 11)
        self.assertEqual(cal_sum(5), 14)

    def test_edge(self):
        self.assertEqual(cal_sum(-1), 3)
        self.assertEqual(cal_sum(0), 3)
        self.assertEqual(cal_sum(1), 3)
        self.assertEqual(cal_sum(2), 5)
        self.assertEqual(cal_sum(3), 8)
        self.assertEqual(cal_sum(4), 11)
        self.assertEqual(cal_sum(5), 14)

    def test_edge2(self):
        self.assertEqual(cal_sum(6), 16)
        self.assertEqual(cal_sum(7), 20)
        self.assertEqual(cal_sum(8), 24)
        self.assertEqual(cal_sum(9), 28)
        self.assertEqual(cal_sum(10), 32)

    def test_edge3(self):
        self.assertEqual(cal_sum(11), 36)
        self.assertEqual(cal_sum(12), 40)
        self.assertEqual(cal_sum(13), 44)
        self.assertEqual(cal_sum(14), 48)
        self.assertEqual(cal_sum(15), 52)

    def test_edge4(self):
        self.assertEqual(cal_sum(16), 56)
        self.assertEqual(cal_sum(17), 60)
        self.assertEqual(cal_sum(18), 64)
        self.assertEqual(cal_sum(19), 68)
        self.assertEqual(cal_sum(20), 72)
