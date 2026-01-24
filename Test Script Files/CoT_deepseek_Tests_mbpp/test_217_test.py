import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(first_Repeated_Char('abcabc'), 'a')
        self.assertEqual(first_Repeated_Char('abcd'), '\0')

    def test_edge_cases(self):
        self.assertEqual(first_Repeated_Char(''), '\0')
        self.assertEqual(first_Repeated_Char('a'), 'a')
        self.assertEqual(first_Repeated_Char('aaa'), 'a')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_Repeated_Char(123)
        with self.assertRaises(TypeError):
            first_Repeated_Char(None)
        with self.assertRaises(TypeError):
            first_Repeated_Char(True)
        with self.assertRaises(TypeError):
            first_Repeated_Char([1, 2, 3])
        with self.assertRaises(TypeError):
            first_Repeated_Char({'a': 1, 'b': 2})
