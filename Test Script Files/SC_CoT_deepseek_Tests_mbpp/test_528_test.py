import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_typical_case(self):
        list1 = ['hello', 'world', 'python']
        self.assertEqual(min_length(list1), (5, 'hello'))

    def test_empty_list(self):
        list1 = []
        self.assertEqual(min_length(list1), (0, ''))

    def test_single_element_list(self):
        list1 = ['single']
        self.assertEqual(min_length(list1), (6, 'single'))

    def test_identical_elements(self):
        list1 = ['same', 'same', 'same']
        self.assertEqual(min_length(list1), (3, 'same'))

    def test_longest_string(self):
        list1 = ['longest', 'short', 'medium']
        self.assertEqual(min_length(list1), (8, 'longest'))

    def test_numeric_strings(self):
        list1 = ['12345', '6789', '10']
        self.assertEqual(min_length(list1), (5, '12345'))

    def test_empty_strings(self):
        list1 = ['', ' ', '   ']
        self.assertEqual(min_length(list1), (0, ''))

    def test_special_characters(self):
        list1 = ['!@#$%', '^&*()', '+_=']
        self.assertEqual(min_length(list1), (5, '!@#$%'))

    def test_mixed_case_strings(self):
        list1 = ['MixedCase', 'lowercase', 'UPPERCASE']
        self.assertEqual(min_length(list1), (8, 'lowercase'))

    def test_unicode_strings(self):
        list1 = ['日本語', 'English', 'Français']
        self.assertEqual(min_length(list1), (3, '日本語'))

    def test_none_elements(self):
        list1 = [None, 'hello', None]
        self.assertRaises(TypeError, min_length, list1)
