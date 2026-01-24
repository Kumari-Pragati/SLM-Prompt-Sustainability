import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_positive_base_and_power(self):
        """Test correct sum for positive base and power"""
        self.assertEqual(power_base_sum(2, 3), 8)
        self.assertEqual(power_base_sum(3, 2), 18)
        self.assertEqual(power_base_sum(5, 4), 91)

    def test_zero_base_and_power(self):
        """Test correct sum for zero base and power"""
        self.assertEqual(power_base_sum(0, 0), 0)
        self.assertEqual(power_base_sum(0, 1), 0)
        self.assertEqual(power_base_sum(0, 2), 0)

    def test_negative_base_and_power(self):
        """Test correct sum for negative base and power"""
        self.assertEqual(power_base_sum(-2, 3), -8)
        self.assertEqual(power_base_sum(-3, 2), -18)
        self.assertEqual(power_base_sum(-5, 4), -91)

    def test_base_equal_to_one(self):
        """Test correct sum for base equal to 1"""
        self.assertEqual(power_base_sum(1, 0), 0)
        self.assertEqual(power_base_sum(1, 1), 1)
        self.assertEqual(power_base_sum(1, 2), 2)

    def test_power_equal_to_one(self):
        """Test correct sum for power equal to 1"""
        self.assertEqual(power_base_sum(2, 1), 2)
        self.assertEqual(power_base_sum(3, 1), 3)
        self.assertEqual(power_base_sum(5, 1), 5)

    def test_negative_input(self):
        """Test correct handling of negative inputs"""
        with self.assertRaises(ValueError):
            power_base_sum(-1, 2)
        with self.assertRaises(ValueError):
            power_base_sum(2, -1)
