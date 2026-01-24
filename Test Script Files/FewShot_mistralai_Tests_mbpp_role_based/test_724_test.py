import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):
    def test_base_1_power_0(self):
        self.assertEqual(power_base_sum(1, 0), 1)

    def test_base_1_power_1(self):
        self.assertEqual(power_base_sum(1, 1), 1)

    def test_base_2_power_2(self):
        self.assertEqual(power_base_sum(2, 2), 7)

    def test_base_3_power_3(self):
        self.assertEqual(power_base_sum(3, 3), 51)

    def test_base_10_power_4(self):
        self.assertEqual(power_base_sum(10, 4), 16)

    def test_negative_base(self):
        with self.assertRaises(ValueError):
            power_base_sum(-2, 3)

    def test_zero_base(self):
        with self.assertRaises(ValueError):
            power_base_sum(0, 3)

    def test_non_integer_base(self):
        with self.assertRaises(TypeError):
            power_base_sum(3.14, 2)

    def test_non_integer_power(self):
        with self.assertRaises(TypeError):
            power_base_sum(2, 3.14)
