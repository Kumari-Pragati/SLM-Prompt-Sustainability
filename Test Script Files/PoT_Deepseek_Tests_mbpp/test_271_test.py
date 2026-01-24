import unittest
from mbpp_271_code import even_Power_Sum

class TestEvenPowerSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(even_Power_Sum(1), 2**10)
        self.assertEqual(even_Power_Sum(2), 2**10 + 2**12)
        self.assertEqual(even_Power_Sum(3), 2**10 + 2**12 + 2**14)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(even_Power_Sum(0), 0)
        self.assertEqual(even_Power_Sum(10), 2**10 + 2**12 + 2**14 + 2**16 + 2**18 + 2**20 + 2**22 + 2**24 + 2**26 + 2**28)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            even_Power_Sum('a')
        with self.assertRaises(ValueError):
            even_Power_Sum(-1)
