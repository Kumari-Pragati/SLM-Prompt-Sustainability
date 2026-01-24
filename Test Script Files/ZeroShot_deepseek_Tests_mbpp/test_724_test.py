import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_power_base_sum(self):
        self.assertEqual(power_base_sum(2, 3), 8)
        self.assertEqual(power_base_sum(3, 2), 9)
        self.assertEqual(power_base_sum(10, 1), 1)
        self.assertEqual(power_base_sum(10, 2), 1)
        self.assertEqual(power_base_sum(100, 3), 5)
        self.assertEqual(power_base_sum(1000, 2), 1)
