import unittest
from mbpp_217_code import first_Repeated_Char

class TestFirstRepeatedChar(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(first_Repeated_Char('abcabc'), 'a')
        self.assertEqual(first_Repeated_Char('abcd'), '\0')
    
    def test_edge_case(self):
        self.assertEqual(first_Repeated_Char(''), '\0')
        self.assertEqual(first_Repeated_Char('a'), 'a')
    
    def test_corner_case(self):
        self.assertEqual(first_Repeated_Char('aabbcc'), 'a')
        self.assertEqual(first_Repeated_Char('abcabcabc'), 'a')
    
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_Repeated_Char(12345)
        with self.assertRaises(TypeError):
            first_Repeated_Char(['a', 'b', 'c'])
