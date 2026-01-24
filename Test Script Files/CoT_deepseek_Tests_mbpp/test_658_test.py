import unittest
from mbpp_658_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)
        
    def test_single_element(self):
        self.assertEqual(max_occurrences([1]), 1)
        
    def test_empty_list(self):
        self.assertIsNone(max_occurrences([]))
        
    def test_negative_numbers(self):
        self.assertEqual(max_occurrences([-1, -1, -2, -2]), -1)
        
    def test_duplicates(self):
        self.assertEqual(max_occurrences([1, 1, 2, 2, 3, 3]), 1)
        
    def test_large_numbers(self):
        self.assertEqual(max_occurrences(list(range(1, 10001))), 1)
        
    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            max_occurrences([1, 2, 2, 'a', 'b', 'b'])
            
    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            max_occurrences('12345')
