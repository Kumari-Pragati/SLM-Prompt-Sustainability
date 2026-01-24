import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]), 
                         [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)])
        
    def test_single_element(self):
        self.assertEqual(sort_list_last([(2, 1)]), [(2, 1)])
        
    def test_empty_list(self):
        self.assertEqual(sort_list_last([]), [])
        
    def test_same_last_elements(self):
        self.assertEqual(sort_list_last([(2, 5), (1, 5), (4, 5), (2, 5), (2, 5)]), 
                         [(2, 5), (1, 5), (4, 5), (2, 5), (2, 5)])
        
    def test_negative_numbers(self):
        self.assertEqual(sort_list_last([(2, -1), (1, -2), (4, -4), (2, -3), (2, -5)]), 
                         [(2, -5), (1, -2), (2, -3), (4, -4), (2, -1)])
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_list_last("not a list")
