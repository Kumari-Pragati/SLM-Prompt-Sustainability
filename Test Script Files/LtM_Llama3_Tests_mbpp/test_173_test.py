import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_splchar('Hello, World!'), 'Hello World')
        self.assertEqual(remove_splchar('Hello_World'), 'Hello World')
        self.assertEqual(remove_splchar('Hello'), 'Hello')

    def test_edge(self):
        self.assertEqual(remove_splchar(''), '')
        self.assertEqual(remove_splchar('Hello'), 'Hello')
        self.assertEqual(remove_splchar('1234567890'), '1234567890')

    def test_invalid(self):
        with self.assertRaises(TypeError):
            remove_splchar(None)
        with self.assertRaises(TypeError):
            remove_splchar(123)
