import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_Repeated_Char('abcabc'), 'a')
        self.assertEqual(first_Repeated_Char('abcd'), '\0')

    def test_edge_conditions(self):
        self.assertEqual(first_Repeated_Char(''), '\0')
        self.assertEqual(first_Repeated_Char('a'), 'a')

    def test_complex_cases(self):
        self.assertEqual(first_Repeated_Char('aabbcc'), 'a')
        self.assertEqual(first_Repeated_Char('abcddcba'), 'd')
        self.assertEqual(first_Repeated_Char('abcdefg'), '\0')
