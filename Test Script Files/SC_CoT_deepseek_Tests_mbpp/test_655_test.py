import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(fifth_Power_Sum(5), 4455)

    def test_boundary_case(self):
        self.assertEqual(fifth_Power_Sum(1), 1)

    def test_edge_case(self):
        self.assertEqual(fifth_Power_Sum(0), 0)
        self.assertEqual(fifth_Power_Sum(-1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            fifth_Power_Sum('5')
        with self.assertRaises(TypeError):
            fifth_Power_Sum(None)
