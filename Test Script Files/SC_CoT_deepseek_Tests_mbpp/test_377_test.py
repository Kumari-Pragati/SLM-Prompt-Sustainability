import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_Char('hello', 'l'), 'heo')

    def test_edge_case(self):
        self.assertEqual(remove_Char('', 'a'), '')
        self.assertEqual(remove_Char('a', 'a'), '')
        self.assertEqual(remove_Char('aaaa', 'a'), '')

    def test_boundary_case(self):
        self.assertEqual(remove_Char('a' * 10000, 'a'), '')

    def test_special_case(self):
        self.assertEqual(remove_Char('hello world', ' '), 'helloworld')
        self.assertEqual(remove_Char('1234567890', '1'), '234567890')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_Char(123, 'a')
        with self.assertRaises(TypeError):
            remove_Char('abc', 123)
