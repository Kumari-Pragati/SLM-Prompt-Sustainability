import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_char_position('HelloWorld'), 2)

    def test_edge_case(self):
        self.assertEqual(count_char_position(''), 0)

    def test_boundary_case(self):
        self.assertEqual(count_char_position('AaBbCc'), 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_char_position(123)
