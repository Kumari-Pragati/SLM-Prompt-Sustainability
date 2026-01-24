import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_char_long('Hello world'), ['Hello', 'world'])
        self.assertEqual(find_char_long('Python is awesome'), ['Python', 'awesome'])

    def test_edge_cases(self):
        self.assertEqual(find_char_long(''), [])
        self.assertEqual(find_char_long('a'), [])
        self.assertEqual(find_char_long('1234567890'), [])

    def test_boundary_cases(self):
        self.assertEqual(find_char_long('aaaaa'), ['aaaaa'])
        self.assertEqual(find_char_long('bbbbbb'), ['bbbbbb'])
        self.assertEqual(find_char_long('ccccccccc'), ['ccccccccc'])

    def test_corner_cases(self):
        self.assertEqual(find_char_long('1234567890abcdefghijklmnopqrstuvwxyz'), ['1234567890abcdefghijklmnopqrstuvwxyz'])
        self.assertEqual(find_char_long('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
