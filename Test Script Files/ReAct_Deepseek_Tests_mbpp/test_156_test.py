import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_int_str([('1', '2'), ('3', '4')]), ((1, 2), (3, 4)))

    def test_single_element(self):
        self.assertEqual(tuple_int_str([('5', '6')]), ((5, 6),))

    def test_empty_tuple(self):
        self.assertEqual(tuple_int_str([]), ())

    def test_negative_numbers(self):
        self.assertEqual(tuple_int_str([('-1', '2'), ('3', '-4')]), ((-1, 2), (3, -4)))

    def test_zero(self):
        self.assertEqual(tuple_int_str([('0', '0')]), ((0, 0),))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_int_str([('1', '2'), ('3', 'four')])

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            tuple_int_str([(1, '2'), ('3', '4')])
