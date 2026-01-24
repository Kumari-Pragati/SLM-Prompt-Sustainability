import unittest
from mbpp_534_code import search_literal

class TestSearchLiteral(unittest.TestCase):

    def test_typical_case(self):
        pattern = 'hello'
        text = 'hello world'
        self.assertEqual(search_literal(pattern, text), (0, 5))

    def test_edge_case(self):
        pattern = 'hello'
        text = 'world'
        self.assertEqual(search_literal(pattern, text), None)

    def test_boundary_case(self):
        pattern = 'hello'
        text = ''
        self.assertEqual(search_literal(pattern, text), None)

    def test_invalid_input(self):
        pattern = 123
        text = 'hello world'
        with self.assertRaises(TypeError):
            search_literal(pattern, text)

        pattern = 'hello'
        text = 123
        with self.assertRaises(TypeError):
            search_literal(pattern, text)
