import unittest
from mbpp_724_code import power_base_sum

class TestPowerBaseSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(power_base_sum(2, 3), 8)
        self.assertEqual(power_base_sum(3, 2), 18)
        self.assertEqual(power_base_sum(4, 4), 64)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(power_base_sum(2, 0), 0)
        self.assertEqual(power_base_sum(2, 1), 2)
        self.assertEqual(power_base_sum(2, -1), 2)
        self.assertEqual(power_base_sum(0, 2), 0)
        self.assertEqual(power_base_sum(1, 0), 1)
