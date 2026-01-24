import unittest
from mbpp_717_code import avg_calc

class Test717Code(unittest.TestCase):

    def test_avg_calc_typical(self):
        self.assertEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)

    def test_avg_calc_single_element(self):
        self.assertEqual(avg_calc([1]), 1.0)

    def test_avg_calc_empty_list(self):
        with self.assertRaises(IndexError):
            avg_calc([])

    def test_avg_calc_sd_calc_typical(self):
        data = [1, 2, 3, 4, 5]
        mean = avg_calc(data)
        sd = sd_calc(data)
        self.assertAlmostEqual(sd, math.sqrt((sum((x - mean) ** 2 for x in data) / (len(data) - 1))), places=5)

    def test_avg_calc_sd_calc_single_element(self):
        data = [1]
        mean = avg_calc(data)
        sd = sd_calc(data)
        self.assertAlmostEqual(sd, 0.0, places=5)

    def test_avg_calc_sd_calc_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            sd_calc([])
