import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(avg_calc([0, 1, 2, 3, 4]), 2.0)
        self.assertAlmostEqual(avg_calc([-1, 0, 1, 2, 3]), 0.0)

    def test_edge_cases(self):
        self.assertEqual(avg_calc([]), sys.float_info.min)
        self.assertEqual(avg_calc([0]), 0.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            avg_calc(123)

    def test_sd_calc_normal_input(self):
        self.assertAlmostEqual(sd_calc([1, 2, 3, 4, 5]), 1.5811388300841898)
        self.assertAlmostEqual(sd_calc([0, 1, 2, 3, 4]), 1.7320508075688772)
        self.assertAlmostEqual(sd_calc([-1, 0, 1, 2, 3]), 1.5811388300841898)

    def test_sd_calc_edge_cases(self):
        self.assertEqual(sd_calc([]), 0.0)
        self.assertEqual(sd_calc([0]), 0.0)

    def test_sd_calc_invalid_input(self):
        with self.assertRaises(TypeError):
            sd_calc(123)
