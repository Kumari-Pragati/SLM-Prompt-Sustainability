import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(power_base_sum(2, 3), 12)

    def test_edge_case_power_zero(self):
        self.assertEqual(power_base_sum(2, 0), 0)

    def test_edge_case_base_one(self):
        self.assertEqual(power_base_sum(1, 3), 1)

    def test_edge_case_power_negative(self):
        with self.assertRaises(TypeError):
            power_base_sum(-2, 3)

    def test_edge_case_base_negative(self):
        with self.assertRaises(TypeError):
            power_base_sum(2, -3)

    def test_edge_case_power_and_base_zero(self):
        self.assertEqual(power_base_sum(0, 0), 0)

    def test_edge_case_power_and_base_negative(self):
        with self.assertRaises(TypeError):
            power_base_sum(-2, -3)
