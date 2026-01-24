import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 134)
        self.assertEqual(fifth_Power_Sum(3), 1441)

    def test_edge_cases(self):
        self.assertEqual(fifth_Power_Sum(0), 0)

    def test_boundary_cases(self):
        self.assertEqual(fifth_Power_Sum(10), 20511784)
        self.assertEqual(fifth_Power_Sum(100), 33422020100L)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            fifth_Power_Sum('a')
        with self.assertRaises(TypeError):
            fifth_Power_Sum(None)
        with self.assertRaises(TypeError):
            fifth_Power_Sum([])
