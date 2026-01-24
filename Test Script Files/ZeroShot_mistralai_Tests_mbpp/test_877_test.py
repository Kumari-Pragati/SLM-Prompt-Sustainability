import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(sort_String(''), '')

    def test_single_character_string(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(sort_String(char), char)

    def test_multiple_characters_string(self):
        test_strings = [
            'zebra',
            'Apple',
            'banana',
            'Cherry',
            'orange',
            'strawberry',
            'racecar',
            'hello',
            'world',
            'Python',
        ]
        for test_string in test_strings:
            sorted_string = ''.join(sorted(test_string))
            self.assertEqual(sort_String(test_string), sorted_string)
