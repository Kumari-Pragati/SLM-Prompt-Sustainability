import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):

    def test_lobb_num_positive_integers(self):
        self.assertEqual(lobb_num(5, 3), 210)
        self.assertEqual(lobb_num(10, 5), 1925)
        self.assertEqual(lobb_num(15, 7), 185640)

    def test_lobb_num_zero(self):
        self.assertEqual(lobb_num(0, 0), 1)

    def test_lobb_num_negative_integers(self):
        self.assertEqual(lobb_num(-5, -3), 0)
        self.assertEqual(lobb_num(-10, -5), 0)
        self.assertEqual(lobb_num(-15, -7), 0)

    def test_lobb_num_negative_and_positive(self):
        self.assertEqual(lobb_num(-5, 3), 0)
        self.assertEqual(lobb_num(5, -3), 0)

    def test_lobb_num_large_integers(self):
        self.assertEqual(lobb_num(100, 50), 1264106064377581730723888420387772631866656937801383272562477255714947337189538720)
