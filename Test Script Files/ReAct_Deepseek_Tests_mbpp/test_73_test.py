import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(multiple_split('a,b*c;d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_empty_string(self):
        self.assertEqual(multiple_split(''), [])

    def test_no_delimiters(self):
        self.assertEqual(multiple_split('abcde'), ['abcde'])

    def test_multiple_delimiters(self):
        self.assertEqual(multiple_split('a*b,c;d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_delimiters_at_start_and_end(self):
        self.assertEqual(multiple_split('*a,b;c\nd\ne*'), ['a', 'b', 'c', 'd', 'e'])

    def test_delimiters_only(self):
        self.assertEqual(multiple_split('*;,'), [])

    def test_delimiters_in_middle(self):
        self.assertEqual(multiple_split('a*b,c;d\ne*f,g'), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
