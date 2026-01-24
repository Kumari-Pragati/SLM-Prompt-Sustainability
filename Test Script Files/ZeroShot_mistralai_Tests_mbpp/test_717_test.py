import unittest
from mbpp_717_code import avg_calc, sd_calc

class TestFunctions(unittest.TestCase):

    def test_avg_calc(self):
        self.assertEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(avg_calc([1, 2, 3]), 2.0)
        self.assertEqual(avg_calc([1]), 1.0)
        self.assertEqual(avg_calc([]), 0.0)

    def test_sd_calc(self):
        self.assertAlmostEqual(sd_calc([1, 2, 3, 4, 5]), 1.5811388300841898)
        self.assertAlmostEqual(sd_calc([1, 2, 3]), 1.2589254123072759)
        self.assertAlmostEqual(sd_calc([1, 2, 3, 1, 2, 3]), 1.0606601717798023)
        self.assertEqual(sd_calc([1]), 0.0)
        self.assertEqual(sd_calc([]), 0.0)
