import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):
    def test_simple_input(self):
        self.assertAlmostEqual(sum_num([1, 2, 3]), 2.0)
        self.assertAlmostEqual(sum_num([4, 4, 4]), 4.0)

    def test_edge_input(self):
        self.assertAlmostEqual(sum_num([0, 0, 0]), 0.0)
        self.assertAlmostEqual(sum_num([1000000000000000000,]), 1.0e-308)

    def test_complex_input(self):
        self.assertAlmostEqual(sum_num([1, -2, 3, -4]), 1.0)
        self.assertAlmostEqual(sum_num([1.1, 2.2, 3.3]), 2.2)
        self.assertAlmostEqual(sum_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5)
