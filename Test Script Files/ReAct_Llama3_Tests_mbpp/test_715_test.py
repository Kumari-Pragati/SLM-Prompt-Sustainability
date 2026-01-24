import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(str_to_tuple("1, 2, 3"), (1, 2, 3))

    def test_edge_case_empty_string(self):
        self.assertEqual(str_to_tuple(""), ())

    def test_edge_case_single_element(self):
        self.assertEqual(str_to_tuple("1"), (1,))

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(str_to_tuple(" 1, 2, 3 "), (1, 2, 3))

    def test_edge_case_leading_trailing_spaces(self):
        self.assertEqual(str_to_tuple(" 1, 2, 3 "), (1, 2, 3))

    def test_edge_case_invalid_input(self):
        with self.assertRaises(ValueError):
            str_to_tuple("not a number")

    def test_edge_case_multiple_invalid_inputs(self):
        with self.assertRaises(ValueError):
            str_to_tuple("not a number, not a number, not a number")
