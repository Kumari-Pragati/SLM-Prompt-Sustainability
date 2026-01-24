import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(sum_in_Range(1, 10), 26)
        
    def test_edge_case_l_equals_r(self):
        self.assertEqual(sum_in_Range(5, 5), 0)
        
    def test_boundary_case_l_less_than_1(self):
        self.assertEqual(sum_in_Range(0, 10), 26)
        
    def test_boundary_case_r_greater_than_100(self):
        self.assertEqual(sum_in_Range(1, 101), 26)
        
    def test_special_case_l_greater_than_r(self):
        self.assertEqual(sum_in_Range(10, 1), 0)
        
    def test_invalid_input_l_not_integer(self):
        with self.assertRaises(TypeError):
            sum_in_Range("a", 10)
            
    def test_invalid_input_r_not_integer(self):
        with self.assertRaises(TypeError):
            sum_in_Range(1, "b")
            
    def test_invalid_input_l_less_than_1(self):
        with self.assertRaises(ValueError):
            sum_in_Range(-1, 10)
            
    def test_invalid_input_r_greater_than_100(self):
        with self.assertRaises(ValueError):
            sum_in_Range(1, 101)
