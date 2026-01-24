import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(2), -1)
        self.assertEqual(sum_difference(3), -4)
        self.assertEqual(sum_difference(4), -9)
        self.assertEqual(sum_difference(5), -16)

    def test_edge(self):
        self.assertEqual(sum_difference(0), 0)
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(10), 251)

    def test_edge2(self):
        self.assertEqual(sum_difference(-1), 0)
        self.assertEqual(sum_difference(-2), 4)
        self.assertEqual(sum_difference(-3), 9)

    def test_edge3(self):
        self.assertEqual(sum_difference(100), 25125)
        self.assertEqual(sum_difference(200), 408050)

    def test_edge4(self):
        self.assertEqual(sum_difference(1000), 2512500)
        self.assertEqual(sum_difference(2000), 4080500)

    def test_edge5(self):
        self.assertEqual(sum_difference(10000), 25125000)
        self.assertEqual(sum_difference(20000), 40805000)
