import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(power_base_sum(2, 3), 8)
        self.assertEqual(power_base_sum(3, 2), 18)
        self.assertEqual(power_base_sum(4, 4), 64)

    def test_edge_cases(self):
        self.assertEqual(power_base_sum(0, 0), 0)
        self.assertEqual(power_base_sum(1, 0), 1)
        self.assertEqual(power_base_sum(2, 0), 2)
        self.assertEqual(power_base_sum(3, 0), 3)
        self.assertEqual(power_base_sum(4, 0), 4)
        self.assertEqual(power_base_sum(5, 0), 5)

        self.assertEqual(power_base_sum(2, 1), 2)
        self.assertEqual(power_base_sum(3, 1), 3)
        self.assertEqual(power_base_sum(4, 1), 4)
        self.assertEqual(power_base_sum(5, 1), 5)

        self.assertEqual(power_base_sum(2, -1), 2)
        self.assertEqual(power_base_sum(3, -1), 3)
        self.assertEqual(power_base_sum(4, -1), 4)
        self.assertEqual(power_base_sum(5, -1), 5)

    def test_negative_base(self):
        self.assertEqual(power_base_sum(-2, 3), -64)
        self.assertEqual(power_base_sum(-3, 2), -18)
        self.assertEqual(power_base_sum(-4, 4), -256)

    def test_negative_power(self):
        self.assertEqual(power_base_sum(2, -3), 2)
        self.assertEqual(power_base_sum(3, -2), 9)
        self.assertEqual(power_base_sum(4, -4), 64)
