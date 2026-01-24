import unittest
from mbpp_146_code import ascii_value_string

class TestAsciiValueString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(ascii_value_string(''), 0)

    def test_single_character_string(self):
        for char in range(128):
            self.assertEqual(ascii_value_string(str(char)), char)

    def test_multi_character_string(self):
        test_strings = [
            'abc', 'ABC', '123', '!@#', 'abcABC123!@#', '🐶🐺🐱'
        ]
        for test_string in test_strings:
            result = 0
            for char in test_string:
                result += ord(char)
            self.assertEqual(ascii_value_string(test_string), result)
