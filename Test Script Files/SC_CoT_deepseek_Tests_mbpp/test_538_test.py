import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(string_list_to_tuple(['abc', 'def', 'ghi']), ('abc', 'def', 'ghi'))
        
    def test_empty_list(self):
        self.assertEqual(string_list_to_tuple([]), ())
        
    def test_list_with_spaces(self):
        self.assertEqual(string_list_to_tuple(['abc def', 'ghi jkl']), ('abcdef', 'ghi jkl'))
        
    def test_list_with_single_space(self):
        self.assertEqual(string_list_to_tuple(['abc def']), ('abcdef',))
        
    def test_list_with_multiple_spaces(self):
        self.assertEqual(string_list_to_tuple(['abc   def']), ('abcdef',))
        
    def test_list_with_special_characters(self):
        self.assertEqual(string_list_to_tuple(['abc!def', 'ghi@jkl']), ('abc!def', 'ghi@jkl'))
        
    def test_list_with_numbers(self):
        self.assertEqual(string_list_to_tuple(['abc1def', 'ghi2jkl']), ('abc1def', 'ghi2jkl'))
        
    def test_list_with_mixed_characters(self):
        self.assertEqual(string_list_to_tuple(['abc123', 'def456']), ('abc123', 'def456'))
        
    def test_list_with_mixed_case(self):
        self.assertEqual(string_list_to_tuple(['AbC', 'DeF', 'GhI']), ('AbC', 'DeF', 'GhI'))
        
    def test_list_with_mixed_spaces_and_characters(self):
        self.assertEqual(string_list_to_tuple(['abc def123', 'ghi jkl456']), ('abc def123', 'ghi jkl456'))
        
    def test_list_with_only_spaces(self):
        self.assertEqual(string_list_to_tuple(['   ', '    ']), ('   ', '    '))
        
    def test_list_with_none(self):
        self.assertEqual(string_list_to_tuple([None]), ())
        
    def test_list_with_empty_string(self):
        self.assertEqual(string_list_to_tuple(['']), ())
