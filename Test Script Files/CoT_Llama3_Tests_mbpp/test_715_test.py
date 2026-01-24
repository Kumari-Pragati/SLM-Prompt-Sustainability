import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(str_to_tuple("1, 2, 3"), (1, 2, 3))

    def test_edge_case_empty_string(self):
        self.assertEqual(str_to_tuple(""), ())

    def test_edge_case_single_element(self):
        self.assertEqual(str_to_tuple("1"), (1,))

    def test_edge_case_single_element_with_spaces(self):
        self.assertEqual(str_to_tuple(" 1  "), (1,))

    def test_edge_case_multiple_elements_with_spaces(self):
        self.assertEqual(str_to_tuple("1, 2, 3"), (1, 2, 3))

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            str_to_tuple(123)

    def test_invalid_input_non_comma_separated_string(self):
        with self.assertRaises(ValueError):
            str_to_tuple("1 2 3")
