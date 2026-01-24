import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(tuple_to_int(()), 0)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(tuple_to_int((5,)), 5)

    def test_edge_case_single_element_tuple_with_zero(self):
        self.assertEqual(tuple_to_int((0,)), 0)

    def test_edge_case_single_element_tuple_with_negative(self):
        self.assertEqual(tuple_to_int((-5,)), -5)

    def test_edge_case_multiple_elements_tuple(self):
        self.assertEqual(tuple_to_int((1, 2, 3, 4, 5)), 12345)

    def test_edge_case_multiple_elements_tuple_with_zero(self):
        self.assertEqual(tuple_to_int((1, 2, 0, 4, 5)), 12045)

    def test_edge_case_multiple_elements_tuple_with_negative(self):
        self.assertEqual(tuple_to_int((-1, -2, -3, -4, -5)), -12345)

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            tuple_to_int("abc")

    def test_invalid_input_tuple_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            tuple_to_int(("a", 2, 3))
