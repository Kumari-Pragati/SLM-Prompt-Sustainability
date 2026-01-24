import unittest
from mbpp_554_code import Split

class TestSplitFunction(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [1, 3, 5])
        
    def test_empty_list(self):
        self.assertEqual(Split([]), [])
        
    def test_all_even_numbers(self):
        self.assertEqual(Split([2, 4, 6, 8]), [])
        
    def test_all_odd_numbers(self):
        self.assertEqual(Split([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])
        
    def test_mixed_numbers(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])
        
    def test_negative_numbers(self):
        self.assertEqual(Split([-1, -2, -3, -4, -5]), [-1, -3, -5])
        
    def test_zero(self):
        self.assertEqual(Split([0]), [])
        
    def test_large_numbers(self):
        self.assertEqual(Split(list(range(1, 1001, 2))), list(range(1, 1001, 2)))
        
    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            Split([1, 2, '3', 4, 5])
            
    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            Split(123)
