import unittest
from mbpp_565_code import split

class TestSplitFunction(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(split('hello'), ['h', 'e', 'l', 'l', 'o'])

    def test_empty_string(self):
        self.assertEqual(split(''), [])

    def test_single_character(self):
        self.assertEqual(split('a'), ['a'])

    def test_multiple_spaces(self):
        self.assertEqual(split('   '), [' ','',''])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            split(123)

    def test_non_string_input2(self):
        with self.assertRaises(TypeError):
            split(None)

    def test_non_string_input3(self):
        with self.assertRaises(TypeError):
            split([1, 2, 3])
