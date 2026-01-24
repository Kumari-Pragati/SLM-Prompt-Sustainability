import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(tuple_int_str(('1', '2')), (1, 2))
        self.assertEqual(tuple_int_str(('3', '4')), (3, 4))

    def test_empty_input(self):
        self.assertRaises(ValueError, tuple_int_str, ())
        self.assertRaises(ValueError, tuple_int_str, [('', '')])

    def test_single_input(self):
        self.assertRaises(ValueError, tuple_int_str, (('1',)))
        self.assertRaises(ValueError, tuple_int_str, (('',)))

    def test_invalid_input(self):
        self.assertRaises(ValueError, tuple_int_str, (('a', 'b'),))
        self.assertRaises(ValueError, tuple_int_str, (('1a', '2b'),))
