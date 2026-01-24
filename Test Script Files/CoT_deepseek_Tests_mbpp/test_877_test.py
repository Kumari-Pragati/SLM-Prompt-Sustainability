import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_String('hello'), 'ehllo')

    def test_empty_string(self):
        self.assertEqual(sort_String(''), '')

    def test_single_character(self):
        self.assertEqual(sort_String('a'), 'a')

    def test_sorted_string(self):
        self.assertEqual(sort_String('abcdef'), 'abcdef')

    def test_numeric_string(self):
        self.assertEqual(sort_String('123456'), '123456')

    def test_special_characters(self):
        self.assertEqual(sort_String('!@#$%^&*()'), '!()%^&*@#$%')

    def test_mixed_case(self):
        self.assertEqual(sort_String('HeLlO'), 'HeLO')

    def test_duplicate_characters(self):
        self.assertEqual(sort_String('aabbcc'), 'aabbcc')

    def test_none_input(self):
        with self.assertRaises(TypeError):
            sort_String(None)
