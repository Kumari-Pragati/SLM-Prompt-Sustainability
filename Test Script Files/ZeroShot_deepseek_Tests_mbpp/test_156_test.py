import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(tuple_int_str(('123', '456')), ((1, 2, 3), (4, 5, 6)))
        self.assertEqual(tuple_int_str(('789', '012')), ((7, 8, 9), (0, 1, 2)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_int_str(123)
        with self.assertRaises(TypeError):
            tuple_int_str('123')
        with self.assertRaises(TypeError):
            tuple_int_str(('123', 456))

    def test_empty_input(self):
        self.assertEqual(tuple_int_str(()), ())
