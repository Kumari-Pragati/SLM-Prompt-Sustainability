import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(string_list_to_tuple(['a', 'b', 'c']), ('a', 'b', 'c'))
        
    def test_empty_list(self):
        self.assertEqual(string_list_to_tuple([]), ())
        
    def test_list_with_spaces(self):
        self.assertEqual(string_list_to_tuple(['a ', ' b', ' c ']), ('a', 'b', 'c'))
        
    def test_list_with_mixed_spaces_and_non_spaces(self):
        self.assertEqual(string_list_to_tuple(['a ', 'b', ' c']), ('a', 'b', 'c'))
        
    def test_list_with_single_space(self):
        self.assertEqual(string_list_to_tuple(['a', ' ', 'b']), ('a', 'b'))
        
    def test_list_with_only_spaces(self):
        self.assertEqual(string_list_to_tuple([' ', ' ', ' ']), ())
        
    def test_list_with_special_characters(self):
        self.assertEqual(string_list_to_tuple(['a!', 'b@', 'c#']), ('a!', 'b@', 'c#'))
        
    def test_list_with_numbers(self):
        self.assertEqual(string_list_to_tuple(['1', '2', '3']), ('1', '2', '3'))
