import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)
        
    def test_negative_numbers(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)
        
    def test_mixed_numbers(self):
        self.assertEqual(max_val([-1, 2, -3, 4, -5]), 4)
        
    def test_empty_list(self):
        self.assertIsNone(max_val([]))
        
    def test_list_with_non_integer_values(self):
        self.assertEqual(max_val([1, 2, '3', 4, 5]), 5)
        
    def test_list_with_duplicates(self):
        self.assertEqual(max_val([1, 2, 2, 4, 5]), 5)
        
    def test_single_integer(self):
        self.assertEqual(max_val([5]), 5)
        
    def test_list_with_none_values(self):
        with self.assertRaises(TypeError):
            max_val([1, 2, None, 4, 5])
