import unittest
from mbpp_717_code import avg_calc, sd_calc

class TestStatistics(unittest.TestCase):
    def test_avg_calc(self):
        self.assertAlmostEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(avg_calc([10, 20, 30]), 20.0)
        self.assertAlmostEqual(avg_calc([1]), 1.0)
        self.assertAlmostEqual(avg_calc([]), 0.0)

    def test_sd_calc(self):
        self.assertAlmostEqual(sd_calc([1, 2, 3, 4, 5]), 1.4142135623730951)
        self.assertAlmostEqual(sd_calc([10, 20, 30]), 10.0)
        self.assertAlmostEqual(sd_calc([1]), 0.0)
        self.assertAlmostEqual(sd_calc([]), 0.0)
