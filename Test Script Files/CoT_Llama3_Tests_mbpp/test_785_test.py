import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(tuple_str_int("1,2,3"), (1, 2, 3))

    def test_edge_case_empty_string(self):
        self.assertEqual(tuple_str_int(""), ())

    def test_edge_case_single_element(self):
        self.assertEqual(tuple_str_int("1"), (1,))

    def test_edge_case_multiple_elements(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5"), (1, 2, 3, 4, 5))

    def test_edge_case_invalid_input(self):
        with self.assertRaises(ValueError):
            tuple_str_int("1,2,3, invalid input")

    def test_edge_case_invalid_input2(self):
        with self.assertRaises(ValueError):
            tuple_str_int("1,2,3,4,5, invalid input")

    def test_edge_case_invalid_input3(self):
        with self.assertRaises(ValueError):
            tuple_str_int("1,2,3,4,5, invalid input, 6")
