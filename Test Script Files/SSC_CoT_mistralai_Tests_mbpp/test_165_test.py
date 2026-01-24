import unittest
from mbpp_165_code import sentinel

from165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(count_char_position('ABCabc123'), 6)
        self.assertEqual(count_char_position('αβγδεζ'), 5)
        self.assertEqual(count_char_position('προσφέρω'), 3)

    def test_edge_cases(self):
        self.assertEqual(count_char_position('A'), 0)
        self.assertEqual(count_char_position('Z'), 0)
        self.assertEqual(count_char_position('a'), 0)
        self.assertEqual(count_char_position('z'), 0)
        self.assertEqual(count_char_position(''), 0)

    def test_boundary_cases(self):
        self.assertEqual(count_char_position('Aa'), 1)
        self.assertEqual(count_char_position('Zz'), 1)
        self.assertEqual(count_char_position('αβ'), 2)
        self.assertEqual(count_char_position('εζ'), 2)
        self.assertEqual(count_char_position('πρ'), 2)

    def test_special_cases(self):
        self.assertEqual(count_char_position('A1'), 1)
        self.assertEqual(count_char_position('Z9'), 1)
        self.assertEqual(count_char_position('α0'), 1)
        self.assertEqual(count_char_position('ε9'), 1)
        self.assertEqual(count_char_position('π7'), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_char_position, 123)
        self.assertRaises(TypeError, count_char_position, sentinel.str_with_special_chars)
