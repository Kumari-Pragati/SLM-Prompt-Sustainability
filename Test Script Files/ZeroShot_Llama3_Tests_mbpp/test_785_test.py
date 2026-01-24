import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(tuple_str_int("(1, 2, 3, 4, 5)"), (1, 2, 3, 4, 5))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            tuple_str_int("Invalid input")

    def test_empty_input(self):
        self.assertEqual(tuple_str_int("()"), ())

    def test_single_element_input(self):
        self.assertEqual(tuple_str_int("(1)"), (1,))

    def test_multiple_elements_input(self):
        self.assertEqual(tuple_str_int("(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    def test_input_with_spaces(self):
        self.assertEqual(tuple_str_int("(1, 2, 3, 4, 5)"), (1, 2, 3, 4, 5))

    def test_input_with_parentheses(self):
        self.assertEqual(tuple_str_int("(1, 2, 3, 4, 5)"), (1, 2, 3, 4, 5))

    def test_input_with_ellipsis(self):
        self.assertEqual(tuple_str_int("(1, 2, 3, 4, 5)"), (1, 2, 3, 4, 5))
