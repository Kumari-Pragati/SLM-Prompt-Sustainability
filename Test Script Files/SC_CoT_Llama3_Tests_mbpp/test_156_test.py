import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(tuple_int_str([('1', '2'), ('3', '4')]), ((1, 2), (3, 2)))

    def test_edge_case_empty_input(self):
        self.assertEqual(tuple_int_str([]), ())

    def test_edge_case_single_element_input(self):
        self.assertEqual(tuple_int_str([('5', '6')]), ((5, 6),))

    def test_edge_case_single_element_input_empty_string(self):
        self.assertEqual(tuple_int_str([('5', '')]), ((5, 0),))

    def test_edge_case_single_element_input_non_numeric(self):
        with self.assertRaises(ValueError):
            tuple_int_str([('5', 'hello')])

    def test_edge_case_multiple_non_numeric(self):
        with self.assertRaises(ValueError):
            tuple_int_str([('5', 'hello'), ('7', 'goodbye')])

    def test_edge_case_mixed_input(self):
        self.assertEqual(tuple_int_str([('1', '2'), ('3', 'hello'), ('4', '5')]), ((1, 2),))

    def test_edge_case_mixed_input_non_numeric(self):
        with self.assertRaises(ValueError):
            tuple_int_str([('1', '2'), ('3', 'hello'), ('4', '5', '6')]))
