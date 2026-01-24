import unittest
from mbpp_676_code import remove_extra_char

class TestRemoveExtraChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_extra_char('Hello World!'), 'HelloWorld')

    def test_empty_input(self):
        self.assertEqual(remove_extra_char(''), '')

    def test_input_with_special_characters(self):
        self.assertEqual(remove_extra_char('Python@3.8'), 'Python38')

    def test_input_with_numbers(self):
        self.assertEqual(remove_extra_char('1234567890'), '1234567890')

    def test_input_with_mixed_characters(self):
        self.assertEqual(remove_extra_char('Python3.8!'), 'Python38')
