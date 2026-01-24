import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertTrue(check_Validity(3, 4, 5))
        
    def test_edge_case_equal_sides(self):
        self.assertTrue(check_Validity(1, 1, 1))
        
    def test_boundary_case_zero(self):
        self.assertTrue(check_Validity(0, 0, 0))
        
    def test_invalid_input_negative_number(self):
        self.assertFalse(check_Validity(-1, 1, 1))
        
    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            check_Validity("a", 1, 1)
            
    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            check_Validity(None, 1, 1)
            
    def test_invalid_input_float(self):
        with self.assertRaises(TypeError):
            check_Validity(1.5, 1, 1)
            
    def test_invalid_input_large_numbers(self):
        with self.assertRaises(OverflowError):
            check_Validity(1e100, 1, 1)
