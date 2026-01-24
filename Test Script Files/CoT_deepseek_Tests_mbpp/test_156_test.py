import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_int_str(('12', '34')), ((12, 34),))

    def test_single_digit(self):
        self.assertEqual(tuple_int_str(('1', '2')), ((1, 2),))

    def test_zero(self):
        self.assertEqual(tuple_int_str(('0', '0')), ((0, 0),))

    def test_negative_numbers(self):
        self.assertEqual(tuple_int_str(('-1', '-2')), ((-1, -2),))

    def test_large_numbers(self):
        self.assertEqual(tuple_int_str(('123456789', '987654321')), ((123456789, 987654321),))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            tuple_int_str(('12a', '34'))

        with self.assertRaises(ValueError):
            tuple_int_str(('12', '34b'))

        with self.assertRaises(ValueError):
            tuple_int_str(('12a34', '56'))

        with self.assertRaises(ValueError):
            tuple_int_str(('1234', '567890'))
