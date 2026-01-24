import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(split_list('EXAMPLETEXT'), ['EXAMPLE', 'TEXT'])

    def test_with_numbers(self):
        self.assertEqual(split_list('EXAMPLE123TEXT'), ['EXAMPLE', '123', 'TEXT'])

    def test_with_special_characters(self):
        self.assertEqual(split_list('EXAMPLE!@#TEXT'), ['EXAMPLE', '!@#', 'TEXT'])

    def test_with_uppercase_letters(self):
        self.assertEqual(split_list('EXAMPLETEXTexampl'), ['EXAMPLETEXT', 'exampl'])

    def test_with_lowercase_letters(self):
        self.assertEqual(split_list('exampletext'), ['exampletext'])

    def test_with_empty_string(self):
        self.assertEqual(split_list(''), [])
