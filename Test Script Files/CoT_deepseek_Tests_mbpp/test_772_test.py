import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_length('Hello World', 5), 'Hello World')

    def test_edge_case(self):
        self.assertEqual(remove_length('Hello World', 0), 'Hello World')

    def test_boundary_case(self):
        self.assertEqual(remove_length('Hello World', 11), '')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_length(12345, 5)
