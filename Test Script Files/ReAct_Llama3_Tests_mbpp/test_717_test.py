import unittest
from mbpp_717_code import avg_calc

class Test717Code(unittest.TestCase):
    def test_avg_calc_single_element(self):
        self.assertEqual(avg_calc([1]), 1)

    def test_avg_calc_multiple_elements(self):
        self.assertAlmostEqual(avg_calc([1, 2, 3, 4, 5]), 3)

    def test_avg_calc_empty_list(self):
        with self.assertRaises(IndexError):
            avg_calc([])

    def test_avg_calc_single_element_list(self):
        self.assertEqual(avg_calc([1]), 1)

    def test_avg_calc_negative_numbers(self):
        self.assertAlmostEqual(avg_calc([-1, -2, -3, -4, -5]), -3)

    def test_avg_calc_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            avg_calc(['a', 'b', 'c'])

    def test_sd_calc_single_element(self):
        self.assertEqual(sd_calc([1]), 0.0)

    def test_sd_calc_multiple_elements(self):
        self.assertAlmostEqual(sd_calc([1, 2, 3, 4, 5]), math.sqrt(2))

    def test_sd_calc_empty_list(self):
        self.assertEqual(sd_calc([]), 0.0)

    def test_sd_calc_single_element_list(self):
        self.assertEqual(sd_calc([1]), 0.0)
