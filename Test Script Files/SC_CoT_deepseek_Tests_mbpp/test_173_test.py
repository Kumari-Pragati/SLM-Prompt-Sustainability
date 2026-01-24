import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSpecialCharacters(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_splchar('Hello, World!'), 'Hello World')

    def test_edge_case(self):
        self.assertEqual(remove_splchar(''), '')

    def test_special_characters(self):
        self.assertEqual(remove_splchar('@#$%^&*()'), '')

    def test_numbers(self):
        self.assertEqual(remove_splchar('1234567890'), '1234567890')

    def test_mixed_case(self):
        self.assertEqual(remove_splchar('Hello, World!1234567890'), 'Hello World1234567890')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_splchar(1234567890)
