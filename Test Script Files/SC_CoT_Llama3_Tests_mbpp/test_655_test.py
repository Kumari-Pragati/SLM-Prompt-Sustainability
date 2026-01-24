import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 32)
        self.assertEqual(fifth_Power_Sum(3), 243)
        self.assertEqual(fifth_Power_Sum(4), 1024)
        self.assertEqual(fifth_Power_Sum(5), 3125)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(fifth_Power_Sum(0), 0)
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(10), 35422484817926191575)
        self.assertEqual(fifth_Power_Sum(20), 35422484817926191575000000)

    def test_special_or_corner_cases(self):
        self.assertEqual(fifth_Power_Sum(-1), 0)
        self.assertEqual(fifth_Power_Sum(-2), 0)
        self.assertEqual(fifth_Power_Sum(0.5), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            fifth_Power_Sum('a')
        with self.assertRaises(TypeError):
            fifth_Power_Sum(None)
