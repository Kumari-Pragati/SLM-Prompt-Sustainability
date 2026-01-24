import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(str_to_tuple("1, 2, 3"), (1, 2, 3))

    def test_empty_string(self):
        self.assertEqual(str_to_tuple(""), ())

    def test_single_element(self):
        self.assertEqual(str_to_tuple("4"), (4,))

    def test_multiple_elements(self):
        self.assertEqual(str_to_tuple("5, 6, 7, 8"), (5, 6, 7, 8))

    def test_non_integer_values(self):
        with self.assertRaises(ValueError):
            str_to_tuple("1, a, 3")

    def test_non_comma_separated_input(self):
        with self.assertRaises(ValueError):
            str_to_tuple("1 2 3")
