import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(count_X((1, 2, 3, 'X', 5, 'X'), 'X'), 2)
        
    def test_single_element_tuple(self):
        self.assertEqual(count_X(('X',), 'X'), 1)
        
    def test_empty_tuple(self):
        self.assertEqual(count_X((), 'X'), 0)
        
    def test_no_match(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 'X'), 0)
        
    def test_case_insensitivity(self):
        self.assertEqual(count_X(('x', 'X', 'x', 'X'), 'X'), 2)
        
    def test_integer_in_tuple(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 1), 1)
        
    def test_negative_integer_in_tuple(self):
        self.assertEqual(count_X((1, -2, 3, -4, -5), -2), 1)
        
    def test_float_in_tuple(self):
        self.assertEqual(count_X((1.1, 2.2, 3.3, 4.4, 5.5), 2.2), 1)
        
    def test_negative_float_in_tuple(self):
        self.assertEqual(count_X((1.1, -2.2, 3.3, -4.4, -5.5), -2.2), 1)
        
    def test_string_in_tuple(self):
        self.assertEqual(count_X(('abc', 'def', 'ghi', 'jkl', 'mno'), 'def'), 1)
        
    def test_empty_string_in_tuple(self):
        self.assertEqual(count_X(('', 'def', 'ghi', 'jkl', 'mno'), ''), 1)
        
    def test_special_characters_in_tuple(self):
        self.assertEqual(count_X(('!@#', '$%^', '&*('), '!@#'), 1)
