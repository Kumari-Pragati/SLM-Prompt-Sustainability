import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(power_base_sum(2, 3), 8)
        self.assertEqual(power_base_sum(3, 2), 18)
        self.assertEqual(power_base_sum(4, 2), 16)

    def test_edge_cases(self):
        self.assertEqual(power_base_sum(2, 0), 0)
        self.assertEqual(power_base_sum(2, 1), 2)
        self.assertEqual(power_base_sum(2, 4), 64)
        self.assertEqual(power_base_sum(10, 1), 1)
        self.assertEqual(power_base_sum(10, 2), 1)
        self.assertEqual(power_base_sum(10, 3), 27)

    def test_negative_base(self):
        self.assertEqual(power_base_sum(-2, 3), -8)
        self.assertEqual(power_base_sum(-3, 2), -18)
        self.assertEqual(power_base_sum(-4, 2), -16)

    def test_floating_point_base(self):
        self.assertEqual(power_base_sum(2.5, 3), 53)
        self.assertEqual(power_base_sum(3.5, 2), 36)
        self.assertEqual(power_base_sum(4.5, 2), 52)
