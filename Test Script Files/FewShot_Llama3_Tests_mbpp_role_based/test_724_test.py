import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):
    def test_power_base_sum_positive_base_positive_power(self):
        self.assertEqual(power_base_sum(2, 3), 8)

    def test_power_base_sum_positive_base_negative_power(self):
        self.assertEqual(power_base_sum(2, -3), 8)

    def test_power_base_sum_negative_base_positive_power(self):
        self.assertEqual(power_base_sum(-2, 3), -8)

    def test_power_base_sum_negative_base_negative_power(self):
        self.assertEqual(power_base_sum(-2, -3), 8)

    def test_power_base_sum_zero_base_positive_power(self):
        self.assertEqual(power_base_sum(0, 3), 0)

    def test_power_base_sum_positive_base_zero_power(self):
        self.assertEqual(power_base_sum(2, 0), 2)

    def test_power_base_sum_negative_base_zero_power(self):
        self.assertEqual(power_base_sum(-2, 0), -2)

    def test_power_base_sum_zero_base_positive_power(self):
        self.assertEqual(power_base_sum(0, 3), 0)

    def test_power_base_sum_zero_base_negative_power(self):
        self.assertEqual(power_base_sum(0, -3), 0)
