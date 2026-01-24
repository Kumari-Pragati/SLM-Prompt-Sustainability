import unittest
from mbpp_717_code import avg_calc

class Test717Code(unittest.TestCase):
    def test_avg_calc_typical(self):
        self.assertAlmostEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)
    def test_avg_calc_single_element(self):
        self.assertEqual(avg_calc([1]), 1.0)
    def test_avg_calc_empty(self):
        with self.assertRaises(IndexError):
            avg_calc([])
    def test_avg_calc_negative(self):
        self.assertAlmostEqual(avg_calc([-1, -2, -3, -4, -5]), -3.0)
    def test_avg_calc_sd_calc(self):
        self.assertAlmostEqual(sd_calc([1, 2, 3, 4, 5]), 1.58113883046)
    def test_avg_calc_sd_calc_single_element(self):
        self.assertEqual(sd_calc([1]), 0.0)
    def test_avg_calc_sd_calc_empty(self):
        with self.assertRaises(IndexError):
            sd_calc([])
    def test_avg_calc_sd_calc_negative(self):
        self.assertAlmostEqual(sd_calc([-1, -2, -3, -4, -5]), 1.58113883046)
