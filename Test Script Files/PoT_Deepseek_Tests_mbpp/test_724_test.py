import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(power_base_sum(2, 3), 8)
        self.assertEqual(power_base_sum(3, 2), 9)
        self.assertEqual(power_base_sum(5, 1), 5)

    def test_edge_cases(self):
        self.assertEqual(power_base_sum(0, 0), 0)
        self.assertEqual(power_base_sum(0, 1), 0)
        self.assertEqual(power_base_sum(1, 0), 1)

    def test_boundary_cases(self):
        self.assertEqual(power_base_sum(10, 1), 1)
        self.assertEqual(power_base_sum(10, 2), 1)
        self.assertEqual(power_base_sum(10, 3), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            power_base_sum("2", 3)
        with self.assertRaises(TypeError):
            power_base_sum(2, "3")
        with self.assertRaises(TypeError):
            power_base_sum("2", "3")
        with self.assertRaises(ValueError):
            power_base_sum(-2, 3)
        with self.assertRaises(ValueError):
            power_base_sum(2, -3)
