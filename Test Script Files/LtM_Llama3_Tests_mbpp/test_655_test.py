import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 32)
        self.assertEqual(fifth_Power_Sum(3), 288)

    def test_edge_cases(self):
        self.assertEqual(fifth_Power_Sum(0), 0)
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(10), 30240)

    def test_large_inputs(self):
        self.assertEqual(fifth_Power_Sum(100), 2432902008176640000)
        self.assertEqual(fifth_Power_Sum(200), 2432902008176640000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            fifth_Power_Sum("a")
        with self.assertRaises(TypeError):
            fifth_Power_Sum(None)
