import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 5), 2)
        
    def test_already_exists(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 3), 1)
        
    def test_insert_at_beginning(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 0), 0)
        
    def test_insert_at_end(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 8), 4)
        
    def test_empty_list(self):
        self.assertEqual(left_insertion([], 5), 0)
        
    def test_negative_numbers(self):
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5, 7], -3), 1)
        
    def test_duplicate_numbers(self):
        self.assertEqual(left_insertion([1, 1, 3, 5, 7], 1), 0)
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            left_insertion("not a list", 5)
