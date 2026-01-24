import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_splchar('Hello, World!'), 'Hello World')

    def test_edge_condition(self):
        self.assertEqual(remove_splchar(''), '')

    def test_boundary_condition(self):
        self.assertEqual(remove_splchar('a' * 10000), 'a' * 10000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_splchar(12345)
