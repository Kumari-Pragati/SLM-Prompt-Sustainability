import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 2), 6)
        
    def test_edge_case_single_element(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 10), 0)
        
    def test_edge_case_two_elements(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2], 2, 2), 3)
        
    def test_edge_case_K_equals_0(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 0), 0)
        
    def test_corner_case_negative_numbers(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([-1, -2, -3, -4], 4, 2), -1)
        
    def test_corner_case_large_numbers(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1000, 2000, 3000, 4000], 4, 5000), 10000)
        
    def test_invalid_input_negative_N(self):
        with self.assertRaises(Exception):
            max_sum_pair_diff_lessthan_K([1, 2, 3, 4], -1, 2)
            
    def test_invalid_input_negative_K(self):
        with self.assertRaises(Exception):
            max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, -1)
            
    def test_invalid_input_empty_array(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 1), 0)
