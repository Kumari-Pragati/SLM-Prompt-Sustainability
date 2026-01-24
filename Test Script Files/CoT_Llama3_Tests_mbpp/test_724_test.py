import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_power_base_sum(self):
        self.assertEqual(power_base_sum(2, 3), 12)
        self.assertEqual(power_base_sum(10, 2), 85)
        self.assertEqual(power_base_sum(5, 1), 5)
        self.assertEqual(power_base_sum(3, 4), 31)
        self.assertEqual(power_base_sum(1, 5), 1)

    def test_power_base_sum_edge_cases(self):
        self.assertEqual(power_base_sum(0, 0), 0)
        self.assertEqual(power_base_sum(0, 1), 0)
        self.assertEqual(power_base_sum(1, 0), 1)
        self.assertEqual(power_base_sum(1, 1), 1)

    def test_power_base_sum_invalid_inputs(self):
        with self.assertRaises(TypeError):
            power_base_sum('a', 2)
        with self.assertRaises(TypeError):
            power_base_sum(2, 'a')
        with self.assertRaises(TypeError):
            power_base_sum('a', 'b')
