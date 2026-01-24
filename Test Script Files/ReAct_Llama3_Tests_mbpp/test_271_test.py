import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_even_power_sum_positive(self):
        self.assertEqual(even_Power_Sum(5), 5760)

    def test_even_power_sum_zero(self):
        self.assertEqual(even_Power_Sum(0), 0)

    def test_even_power_sum_negative(self):
        with self.assertRaises(TypeError):
            even_Power_Sum(-1)

    def test_even_power_sum_non_integer(self):
        with self.assertRaises(TypeError):
            even_Power_Sum(3.5)

    def test_even_power_sum_edge_case(self):
        self.assertEqual(even_Power_Sum(1), 32)
