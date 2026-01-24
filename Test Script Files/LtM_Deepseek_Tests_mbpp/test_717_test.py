import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):

    def test_avg_calc_simple(self):
        self.assertAlmostEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)

    def test_avg_calc_edge(self):
        self.assertEqual(avg_calc([1]), 1)
        self.assertEqual(avg_calc([]), 0)

    def test_avg_calc_complex(self):
        self.assertAlmostEqual(avg_calc([1.5, 2.5, 3.5]), 2.5)
        self.assertAlmostEqual(avg_calc([10, 20, 30, 40, 50]), 30.0)
