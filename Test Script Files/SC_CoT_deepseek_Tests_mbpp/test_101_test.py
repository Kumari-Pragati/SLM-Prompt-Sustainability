import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 6, 3), 7)
    
    def test_edge_case_k_equals_1(self):
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 6, 1), 20)
    
    def test_edge_case_k_equals_n(self):
        self.assertEqual(kth_element([7, 10, 4, 3, 20, 15], 6, 6), 3)
    
    def test_edge_case_n_equals_1(self):
        self.assertEqual(kth_element([7], 1, 1), 7)
    
    def test_invalid_input_k_greater_than_n(self):
        with self.assertRaises(IndexError):
            kth_element([7, 10, 4, 3, 20, 15], 6, 7)
    
    def test_invalid_input_k_less_than_1(self):
        with self.assertRaises(IndexError):
            kth_element([7, 10, 4, 3, 20, 15], 6, 0)
    
    def test_invalid_input_n_less_than_k(self):
        with self.assertRaises(IndexError):
            kth_element([7, 10, 4, 3, 20, 15], 5, 6)
    
    def test_invalid_input_empty_array(self):
        with self.assertRaises(IndexError):
            kth_element([], 0, 1)
