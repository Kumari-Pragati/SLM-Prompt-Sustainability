import unittest
from mbpp_717_code import avg_calc

class TestAvgCalc(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(avg_calc([]), 0.0)

    def test_single_element_list(self):
        for num in [1, -1, 0]:
            self.assertEqual(avg_calc([num]), num)

    def test_positive_numbers(self):
        data = [1.1, 2.2, 3.3, 4.4, 5.5]
        expected_mean = (1.1 + 2.2 + 3.3 + 4.4 + 5.5) / 5.0
        self.assertAlmostEqual(avg_calc(data), expected_mean)

    def test_negative_numbers(self):
        data = [-1.1, -2.2, -3.3, -4.4, -5.5]
        expected_mean = (1.1 + 2.2 + 3.3 + 4.4 + 5.5) / 5.0
        self.assertAlmostEqual(avg_calc(data), expected_mean)

    def test_mixed_numbers(self):
        data = [1.1, -2.2, 3.3, -4.4, 5.5]
        expected_mean = (1.1 + (-2.2) + 3.3 + (-4.4) + 5.5) / 5.0
        self.assertAlmostEqual(avg_calc(data), expected_mean)

    def test_large_data_set(self):
        data = [i for i in range(1000)]
        expected_mean = sum(data) / len(data)
        self.assertAlmostEqual(avg_calc(data), expected_mean)

    def test_sd_calc_with_empty_list(self):
        self.assertEqual(sd_calc([]), 0.0)

    def test_sd_calc_with_single_element_list(self):
        for num in [1, -1, 0]:
            self.assertEqual(sd_calc([num]), 0.0)

    def test_sd_calc_with_positive_numbers(self):
        data = [1.1, 2.2, 3.3, 4.4, 5.5]
        expected_mean = (1.1 + 2.2 + 3.3 + 4.4 + 5.5) / 5.0
        expected_sd = math.sqrt(((1.1 - expected_mean)**2 + (2.2 - expected_mean)**2 + (3.3 - expected_mean)**2 + (4.4 - expected_mean)**2 + (5.5 - expected_mean)**2) / (len(data) - 1))
        self.assertAlmostEqual(sd_calc(data), expected_sd)

    def test_sd_calc_with_negative_numbers(self):
        data = [-1.1, -2.2, -3.3, -4.4, -5.5]
        expected_mean = (1.1 + 2.2 + 3.3 + 4.4 + 5.5) / 5.0
        expected_sd = math.sqrt(((1.1 - expected_mean)**2 + (-2.2 - expected_mean)**2 + (-3.3 - expected_mean)**2 + (-4.4 - expected_mean)**2 + (-5.5 - expected_mean)**2) / (len(data) - 1))
        self.assertAlmostEqual(sd_calc(data), expected_sd)

    def test_sd_calc_with_mixed_numbers(self):
        data = [1.1, -2.2, 3.3, -4.4, 5.5]
        expected_mean = (1.1 + (-2.2) + 3.3 + (-4.4) + 5.5) / 5.0
        expected_sd = math.sqrt(((1.1 - expected_mean)**2 + (-2.2 - expected_mean)**2 + (3.3