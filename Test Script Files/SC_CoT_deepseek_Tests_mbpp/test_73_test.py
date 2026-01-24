import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_empty_string(self):
        self.assertEqual(multiple_split(''), [])

    def test_string_without_delimiters(self):
        self.assertEqual(multiple_split('abcde'), ['abcde'])

    def test_string_with_multiple_delimiters(self):
        self.assertEqual(multiple_split('a*b,c;d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_string_with_newline(self):
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_string_with_trailing_delimiters(self):
        self.assertEqual(multiple_split('a,b;c*d\n, *'), ['a', 'b', 'c', 'd'])

    def test_string_with_leading_delimiters(self):
        self.assertEqual(multiple_split(',*;a b\nc*d\n'), ['', '', '', 'a', 'b', 'c', 'd'])

    def test_string_with_multiple_consecutive_delimiters(self):
        self.assertEqual(multiple_split('a,,,b;c**d\ne'), ['a', '', '', 'b', 'c', '', 'd', 'e'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiple_split(123)
