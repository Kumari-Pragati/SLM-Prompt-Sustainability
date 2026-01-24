import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartAEndB(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_starta_endb('acb'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_starta_endb('ab'), 'Found a match!')

    def test_boundary_case(self):
        self.assertEqual(text_starta_endb('a'), 'Not matched!')
        self.assertEqual(text_starta_endb('b'), 'Not matched!')
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_no_a_or_b(self):
        self.assertEqual(text_starta_endb('xyz'), 'Not matched!')

    def test_multiple_a_and_b(self):
        self.assertEqual(text_starta_endb('abcabc'), 'Found a match!')
        self.assertEqual(text_starta_endb('ababab'), 'Found a match!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_starta_endb(123)
