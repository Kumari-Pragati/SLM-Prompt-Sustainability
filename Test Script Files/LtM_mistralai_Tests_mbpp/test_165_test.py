import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(count_char_position('ABC'), 3)
        self.assertEqual(count_char_position('abc'), 3)
        self.assertEqual(count_char_position('AaBbCc'), 6)

    def test_edge_cases(self):
        self.assertEqual(count_char_position(''), 0)
        self.assertEqual(count_char_position('Z'), 0)
        self.assertEqual(count_char_position('z'), 0)
        self.assertEqual(count_char_position('A'), 0)
        self.assertEqual(count_char_position('a'), 0)

    def test_complex_cases(self):
        self.assertEqual(count_char_position('AaBbCcDdEeFfGgHhIiJj'), 16)
        self.assertEqual(count_char_position('AaBbCcDdEeFfGgHhIiJjKk'), 17)
        self.assertEqual(count_char_position('AaBbCcDdEeFfGgHhIiJjKkLl'), 18)
        self.assertEqual(count_char_position('AaBbCcDdEeFfGgHhIiJjKkLlMm'), 19)
        self.assertEqual(count_char_position('AaBbCcDdEeFfGgHhIiJjKkLlMmNn'), 20)
