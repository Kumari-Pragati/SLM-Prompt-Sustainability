import unittest
from mbpp_717_code import avg_calc, sd_calc

class Test717Code(unittest.TestCase):

    def test_sd_calc_empty_list(self):
        self.assertEqual(sd_calc([]), 0.0)

    def test_sd_calc_single_element_list(self):
        self.assertEqual(sd_calc([1]), 0.0)

    def test_sd_calc_two_elements_list(self):
        self.assertEqual(sd_calc([1, 2]), 0.0)

    def test_sd_calc_three_elements_list(self):
        self.assertEqual(sd_calc([1, 2, 3]), 0.0)

    def test_sd_calc_four_elements_list(self):
        self.assertEqual(sd_calc([1, 2, 3, 4]), 0.0)

    def test_sd_calc_five_elements_list(self):
        self.assertEqual(sd_calc([1, 2, 3, 4, 5]), 0.0)

    def test_avg_calc_empty_list(self):
        self.assertRaises(ZeroDivisionError, avg_calc, [])

    def test_avg_calc_single_element_list(self):
        self.assertEqual(avg_calc([1]), 1.0)

    def test_avg_calc_two_elements_list(self):
        self.assertEqual(avg_calc([1, 2]), 1.5)

    def test_avg_calc_three_elements_list(self):
        self.assertEqual(avg_calc([1, 2, 3]), 2.0)

    def test_avg_calc_four_elements_list(self):
        self.assertEqual(avg_calc([1, 2, 3, 4]), 2.5)

    def test_avg_calc_five_elements_list(self):
        self.assertEqual(avg_calc([1, 2, 3, 4, 5]), 3.0)
