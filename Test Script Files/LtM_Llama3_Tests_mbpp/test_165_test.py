import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count_char_position("Hello"), 2)
        self.assertEqual(count_char_position("hello"), 2)
        self.assertEqual(count_char_position("ABC"), 0)
        self.assertEqual(count_char_position("abc"), 0)

    def test_edge_cases(self):
        self.assertEqual(count_char_position(""), 0)
        self.assertEqual(count_char_position("A"), 1)
        self.assertEqual(count_char_position("a"), 1)
        self.assertEqual(count_char_position("123"), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_char_position(123)
        with self.assertRaises(TypeError):
            count_char_position([1, 2, 3])
