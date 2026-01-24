import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(sum_div(6), 6)
        
    def test_prime_number(self):
        self.assertEqual(sum_div(5), 1)
        
    def test_number_with_single_divisor(self):
        self.assertEqual(sum_div(10), 1)
        
    def test_number_with_multiple_divisors(self):
        self.assertEqual(sum_div(12), 1+2+3+4+6)
        
    def test_boundary_case(self):
        self.assertEqual(sum_div(1), 1)
        
    def test_edge_case(self):
        self.assertEqual(sum_div(0), 0)
        
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sum_div(-10)
            
    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            sum_div(1.5)
