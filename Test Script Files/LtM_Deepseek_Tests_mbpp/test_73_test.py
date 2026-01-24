import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):
    def test_simple_split(self):
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_empty_input(self):
        self.assertEqual(multiple_split(''), [])

    def test_single_character_input(self):
        self.assertEqual(multiple_split('a'), ['a'])

    def test_no_delimiter_input(self):
        self.assertEqual(multiple_split('a,b;c*d\ne'), ['a', 'b', 'c', 'd', 'e'])

    def test_multiple_delimiters_in_a_row(self):
        self.assertEqual(multiple_split('a,,,b;;c**d\n\ne'), ['a', '', 'b', ';', 'c', '**d', 'e'])

    def test_delimiters_at_the_end(self):
        self.assertEqual(multiple_split('a,b;c*d\n'), ['a', 'b', 'c', 'd'])

    def test_delimiters_at_the_beginning(self):
        self.assertEqual(multiple_split(',a;b*c\nd'), [',a', 'b', 'c', 'd'])

    def test_delimiters_only(self):
        self.assertEqual(multiple_split(',;**\n'), ['', '', ''])
