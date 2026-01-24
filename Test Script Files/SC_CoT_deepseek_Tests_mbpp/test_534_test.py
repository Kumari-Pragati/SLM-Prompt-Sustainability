import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_typical_case(self):
        pattern = 'hello'
        text = 'hello world'
        self.assertEqual(search_literal(pattern, text), (0, 5))

    def test_edge_case(self):
        pattern = ''
        text = 'hello world'
        self.assertEqual(search_literal(pattern, text), (0, 0))

    def test_boundary_case(self):
        pattern = 'hello'
        text = ''
        self.assertEqual(search_literal(pattern, text), (-1, -1))

    def test_corner_case(self):
        pattern = 'hello'
        text = 'world'
        self.assertEqual(search_literal(pattern, text), (-1, -1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            search_literal(123, 'hello world')
        with self.assertRaises(TypeError):
            search_literal('hello', 123)
