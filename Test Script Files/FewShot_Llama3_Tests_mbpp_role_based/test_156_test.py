import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tuple_int_str([('1', '2'), ('3', '4')]), ((1, 2), (3, 4)))

    def test_empty_input(self):
        self.assertEqual(tuple_int_str([]), ())

    def test_single_element_input(self):
        self.assertEqual(tuple_int_str([('5', '6')]), ((5, 6),))

    def test_non_integer_values(self):
        with self.assertRaises(ValueError):
            tuple_int_str([('a', 'b'), ('c', 'd')])

    def test_non_string_values(self):
        with self.assertRaises(ValueError):
            tuple_int_str([(1, 2), (3, 4)])

    def test_mixed_input_types(self):
        with self.assertRaises(ValueError):
            tuple_int_str([('1', 2), ('3', '4')])
