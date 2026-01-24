import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):
    def test_power_base_sum_simple(self):
        self.assertEqual(power_base_sum(2, 3), 8)
        self.assertEqual(power_base_sum(3, 2), 9)
        self.assertEqual(power_base_sum(4, 1), 4)
        self.assertEqual(power_base_sum(5, 0), 0)

    def test_power_base_sum_edge(self):
        self.assertEqual(power_base_sum(0, 0), 0)
        self.assertEqual(power_base_sum(1, 0), 0)
        self.assertEqual(power_base_sum(0, 1), 0)
        self.assertEqual(power_base_sum(1, 1), 1)

    def test_power_base_sum_invalid(self):
        with self.assertRaises(TypeError):
            power_base_sum('a', 2)
        with self.assertRaises(TypeError):
            power_base_sum(2, 'a')
        with self.assertRaises(TypeError):
            power_base_sum(None, 2)
        with self.assertRaises(TypeError):
            power_base_sum(2, None)
