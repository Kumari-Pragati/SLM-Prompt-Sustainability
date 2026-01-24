import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):

    def test_fill_spaces_with_comma(self):
        self.assertEqual(fill_spaces('Hello, World'), 'Hello:World')

    def test_fill_spaces_with_space(self):
        self.assertEqual(fill_spaces('Hello World'), 'Hello:World')

    def test_fill_spaces_with_period(self):
        self.assertEqual(fill_spaces('Hello.World'), 'Hello:World')

    def test_fill_spaces_with_comma_and_period(self):
        self.assertEqual(fill_spaces('Hello, World.How are you?'), 'Hello:World:How:are:you')
