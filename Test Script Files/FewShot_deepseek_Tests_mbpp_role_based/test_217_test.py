import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_Repeated_Char('abcabc'), 'a')

    def test_edge_case(self):
        self.assertEqual(first_Repeated_Char(''), '\0')

    def test_boundary_case(self):
        self.assertEqual(first_Repeated_Char('a'*217), 'a')
        self.assertEqual(first_Repeated_Char('a'*218), '\0')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_Repeated_Char(12345)
