import unittest
from mbpp_480_code import get_max_occuring_char

class TestGetMaxOccuringChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_max_occuring_char('aaabbc'), 'a')
        self.assertEqual(get_max_occuring_char('hello'), 'l')
        self.assertEqual(get_max_occuring_char('Python'), 't')

    def test_edge_cases(self):
        self.assertEqual(get_max_occuring_char(''), '')
        self.assertEqual(get_max_occuring_char(' '), ' ')
        self.assertEqual(get_max_occuring_char('A' * 1000), 'A')
        self.assertEqual(get_max_occuring_char('!@#$%^&*()_+-=[]{}|;:,.<>/?~`'), ' ')

    def test_boundary_conditions(self):
        self.assertEqual(get_max_occuring_char('Aa1Bb2Cc3'), '3')
        self.assertEqual(get_max_occuring_char('A\tB\nC'), '\n')
        self.assertEqual(get_max_occuring_char('A\0B\nC'), '\0')
