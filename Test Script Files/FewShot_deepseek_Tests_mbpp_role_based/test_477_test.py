import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(is_lower('Hello'), 'hello')

    def test_edge_case(self):
        self.assertEqual(is_lower(''), '')

    def test_boundary_case(self):
        self.assertEqual(is_lower('A'), 'a')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_lower(123)
