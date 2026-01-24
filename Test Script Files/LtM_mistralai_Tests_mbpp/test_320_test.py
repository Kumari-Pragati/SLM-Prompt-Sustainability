import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(2), 3)
        self.assertEqual(sum_difference(3), 10)
        self.assertEqual(sum_difference(4), 25)

    def test_edge_cases(self):
        self.assertEqual(sum_difference(0), 0)
        self.assertEqual(sum_difference(1000), 3178310000)

    def test_complex(self):
        self.assertEqual(sum_difference(5000), 66807375000000)
        self.assertEqual(sum_difference(10000), 2774877489200000)
