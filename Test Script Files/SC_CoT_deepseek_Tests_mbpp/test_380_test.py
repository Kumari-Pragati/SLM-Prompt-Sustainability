import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(multi_list(3, 3), [[0, 0, 0], [0, 1, 2], [0, 2, 4]])
        
    def test_edge_case_zero_rows(self):
        self.assertEqual(multi_list(0, 3), [])
        
    def test_edge_case_zero_cols(self):
        self.assertEqual(multi_list(3, 0), [[] for _ in range(3)])
        
    def test_edge_case_one_row_one_col(self):
        self.assertEqual(multi_list(1, 1), [[0]])
        
    def test_boundary_case_large_numbers(self):
        self.assertEqual(multi_list(100, 100), [[0 for _ in range(100)] for _ in range(100)])
        
    def test_invalid_input_negative_rows(self):
        with self.assertRaises(Exception):
            multi_list(-3, 3)
            
    def test_invalid_input_negative_cols(self):
        with self.assertRaises(Exception):
            multi_list(3, -3)
            
    def test_invalid_input_non_integer_rows(self):
        with self.assertRaises(Exception):
            multi_list(3.5, 3)
            
    def test_invalid_input_non_integer_cols(self):
        with self.assertRaises(Exception):
            multi_list(3, 3.5)
