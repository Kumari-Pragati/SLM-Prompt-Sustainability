import unittest
from mbpp_634_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(even_Power_Sum(1), 16)
        self.assertEqual(even_Power_Sum(2), 16*16 + 32*32*32*32)
        self.assertEqual(even_Power_Sum(3), 16*16 + 32*32*32*32 + 48*48*48*48)

    def test_boundary_conditions(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(100), sum([(2*i)*(2*i)*(2*i)*(2*i) for i in range(1, 101)]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
        with self.assertRaises(ValueError):
            even_Power_Sum(-1)
