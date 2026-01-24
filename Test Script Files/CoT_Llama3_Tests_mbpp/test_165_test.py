import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_char_position("Hello World"), 2)

    def test_edge_case(self):
        self.assertEqual(count_char_position("abc"), 0)

    def test_edge_case2(self):
        self.assertEqual(count_char_position("ABC"), 0)

    def test_edge_case3(self):
        self.assertEqual(count_char_position("123"), 0)

    def test_edge_case4(self):
        self.assertEqual(count_char_position(""), 0)

    def test_edge_case5(self):
        self.assertEqual(count_char_position("aA"), 2)

    def test_edge_case6(self):
        self.assertEqual(count_char_position("aAaA"), 4)

    def test_edge_case7(self):
        self.assertEqual(count_char_position("aAaAaA"), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_char_position(123)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            count_char_position([1, 2, 3])
