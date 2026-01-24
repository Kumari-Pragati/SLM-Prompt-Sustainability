import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(sort_String('abc'), 'abc')
        self.assertEqual(sort_String('ABC'), 'ABC')
        self.assertEqual(sort_String('123'), '123')
        self.assertEqual(sort_String('!@#$%^&*()'), '!@#$%^&*()')

    def test_edge_cases(self):
        self.assertEqual(sort_String(''), '')
        self.assertEqual(sort_String('a'), 'a')
        self.assertEqual(sort_String('aaaa'), 'aaaaa')
        self.assertEqual(sort_String('z'), 'z')
        self.assertEqual(sort_String('Z'), 'Z')
        self.assertEqual(sort_String('0'), '0')
        self.assertEqual(sort_String('9'), '9')

    def test_complex_cases(self):
        self.assertEqual(sort_String('AaBbCc'), 'AaBbCc')
        self.assertEqual(sort_String('123456789'), '123456789')
        self.assertEqual(sort_String('!@#$%^&*()ABC'), '!@#$%^&*()ABC')
        self.assertEqual(sort_String('ZzYyXx'), 'ZzYyXx')
        self.assertEqual(sort_String('987654321'), '987654321')
