import unittest
from mbpp_269_code import ascii_value

class TestAsciiValue(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(ascii_value('a'), 97)

    def test_edge_condition(self):
        self.assertEqual(ascii_value(' '), 32)

    def test_boundary_condition(self):
        self.assertEqual(ascii_value('~'), 126)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            ascii_value(123)
