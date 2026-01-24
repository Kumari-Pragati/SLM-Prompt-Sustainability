import unittest
from mbpp_456_code import reverse_string_list

class TestReverseStringList(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(reverse_string_list(['abc', 'def']), ['cba', 'fed'])
        
    def test_empty_list(self):
        self.assertEqual(reverse_string_list([]), [])
        
    def test_single_string(self):
        self.assertEqual(reverse_string_list(['abc']), ['cba'])
        
    def test_string_with_spaces(self):
        self.assertEqual(reverse_string_list(['abc def']), ['fed cba'])
        
    def test_special_characters(self):
        self.assertEqual(reverse_string_list(['!@#']), ['#@!'])
        
    def test_numeric_strings(self):
        self.assertEqual(reverse_string_list(['123', '456']), ['321', '654'])
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            reverse_string_list(123)
