import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5]), 1)
        
    def test_single_element(self):
        self.assertEqual(smallest_num([5]), 5)
        
    def test_negative_numbers(self):
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5]), -5)
        
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            smallest_num([])
            
    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            smallest_num("1, 2, 3")
            
    def test_duplicates(self):
        self.assertEqual(smallest_num([5, 5, 5, 5, 5]), 5)
