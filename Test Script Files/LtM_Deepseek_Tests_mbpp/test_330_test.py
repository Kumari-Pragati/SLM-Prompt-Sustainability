import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_char("Hello World"), ['ell', 'o', 'orl', 'Wor', 'rld'])
        self.assertEqual(find_char("Python is fun"), ['ytho', 'fun'])

    def test_edge_conditions(self):
        self.assertEqual(find_char(""), [])
        self.assertEqual(find_char("a"), [])
        self.assertEqual(find_char("123456"), [])
        self.assertEqual(find_char("@#$%^&*()"), [])

    def test_boundary_conditions(self):
        self.assertEqual(find_char("a"*3), ['aaa'])
        self.assertEqual(find_char("a"*4), ['aaaa'])
        self.assertEqual(find_char("a"*5), ['aaaaa'])
        self.assertEqual(find_char("a"*6), ['aaaaaa'])
        self.assertEqual(find_char("a"*7), ['aaaaaaa'])

    def test_complex_cases(self):
        self.assertEqual(find_char("Python3 is fun"), ['ytho', 'fun'])
        self.assertEqual(find_char("1234567890"), [])
        self.assertEqual(find_char("!@#$%^&*()"), [])
