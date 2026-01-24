import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(remove_char('Hello, World!'), 'HelloWorld')
        
    def test_empty_string(self):
        self.assertEqual(remove_char(''), '')
        
    def test_string_with_numbers(self):
        self.assertEqual(remove_char('Python3.8'), 'Python38')
        
    def test_string_with_special_characters(self):
        self.assertEqual(remove_char('@Python$2020'), 'Python2020')
        
    def test_string_with_spaces(self):
        self.assertEqual(remove_char('Hello World'), 'HelloWorld')
        
    def test_string_with_underscore(self):
        self.assertEqual(remove_char('Hello_World'), 'HelloWorld')
        
    def test_string_with_mixed_case(self):
        self.assertEqual(remove_char('Hello WoRlD'), 'HelloWorld')
        
    def test_string_with_mixed_case_and_special_characters(self):
        self.assertEqual(remove_char('H@e@l@l@o World!'), 'HelloWorld')
        
    def test_string_with_mixed_case_numbers_and_special_characters(self):
        self.assertEqual(remove_char('Pyt@hon3.8'), 'Python38')
        
    def test_string_with_special_characters_only(self):
        self.assertEqual(remove_char('@#$%^&*('), '')
