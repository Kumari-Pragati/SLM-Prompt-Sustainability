import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(power_base_sum(2, 3), 8)

    def test_power_one(self):
        self.assertEqual(power_base_sum(2, 1), 2)

    def test_power_zero(self):
        self.assertEqual(power_base_sum(2, 0), 2)

    def test_large_numbers(self):
        self.assertEqual(power_base_sum(100, 2), 4)

    def test_negative_power(self):
        self.assertEqual(power_base_sum(2, -1), 2)

    def test_negative_base(self):
        self.assertEqual(power_base_sum(-2, 3), 8)

    def test_negative_base_and_power(self):
        self.assertEqual(power_base_sum(-2, -1), 2)

    def test_zero_base(self):
        self.assertEqual(power_base_sum(0, 3), 0)

    def test_invalid_power(self):
        with self.assertRaises(TypeError):
            power_base_sum(2, 'a')

    def test_invalid_base(self):
        with self.assertRaises(TypeError):
            power_base_sum('a', 3)
