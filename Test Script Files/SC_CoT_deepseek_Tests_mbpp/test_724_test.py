import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(power_base_sum(2, 3), 8)

    def test_boundary_case(self):
        self.assertEqual(power_base_sum(0, 0), 1)

    def test_edge_case(self):
        self.assertEqual(power_base_sum(1, 1000), 1)
        self.assertEqual(power_base_sum(9, 1000), 9)

    def test_special_case(self):
        self.assertEqual(power_base_sum(3, 2), 9)
        self.assertEqual(power_base_sum(7, 3), 18)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            power_base_sum('a', 2)
        with self.assertRaises(TypeError):
            power_base_sum(2, 'b')
        with self.assertRaises(ValueError):
            power_base_sum(-2, 2)
        with self.assertRaises(ValueError):
            power_base_sum(2, -2)
