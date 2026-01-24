import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(power_base_sum(2, 3), 8)

    def test_boundary_case(self):
        self.assertEqual(power_base_sum(0, 0), 1)

    def test_edge_case(self):
        self.assertEqual(power_base_sum(1, 1000), 1)
        self.assertEqual(power_base_sum(10, 10), 1)

    def test_negative_base(self):
        self.assertEqual(power_base_sum(-2, 3), 8)

    def test_negative_power(self):
        self.assertEqual(power_base_sum(2, -3), 0)

    def test_large_numbers(self):
        self.assertEqual(power_base_sum(100, 2), 1)
