import unittest
from mbpp_855_code import check_Even_Parity

class TestCheckEvenParity(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertTrue(check_Even_Parity(10))
        
    def test_typical_case_odd(self):
        self.assertFalse(check_Even_Parity(7))
        
    def test_boundary_case_zero(self):
        self.assertTrue(check_Even_Parity(0))
        
    def test_boundary_case_negative(self):
        self.assertTrue(check_Even_Parity(-10))
        
    def test_edge_case_max_int(self):
        self.assertTrue(check_Even_Parity(2**31 - 1))
        
    def test_edge_case_min_int(self):
        self.assertFalse(check_Even_Parity(-2**31))
        
    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            check_Even_Parity('abc')
            
    def test_invalid_input_float(self):
        with self.assertRaises(TypeError):
            check_Even_Parity(10.5)
