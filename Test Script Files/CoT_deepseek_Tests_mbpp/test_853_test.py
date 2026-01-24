import unittest
from mbpp_853_code import sum_of_odd_Factors

class TestSumOfOddFactors(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(sum_of_odd_Factors(12), 17)
        
    def test_edge_case_single_factor(self):
        self.assertEqual(sum_of_odd_Factors(25), 26)
        
    def test_edge_case_prime_number(self):
        self.assertEqual(sum_of_odd_Factors(13), 14)
        
    def test_edge_case_power_of_two(self):
        self.assertEqual(sum_of_odd_Factors(16), 17)
        
    def test_invalid_input_negative(self):
        with self.assertRaises(Exception):
            sum_of_odd_Factors(-1)
            
    def test_invalid_input_zero(self):
        with self.assertRaises(Exception):
            sum_of_odd_Factors(0)
            
    def test_invalid_input_non_integer(self):
        with self.assertRaises(Exception):
            sum_of_odd_Factors(1.5)
