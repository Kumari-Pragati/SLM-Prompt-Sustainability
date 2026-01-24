import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsInstance(tuple_int_str(()), tuple)
        self.assertEqual(tuple_int_str(()), ())

    def test_single_element_tuple(self):
        self.assertIsInstance(tuple_int_str(('1', '2')), tuple)
        self.assertEqual(tuple_int_str(('1', '2')), ((1, 2)))

    def test_multiple_elements_tuple(self):
        self.assertIsInstance(tuple_int_str(('1', '2'), ('3', '4'), ('5', '6'))), tuple)
        self.assertEqual(tuple_int_str(('1', '2'), ('3', '4'), ('5', '6')), ((1, 2), (3, 4), (5, 6)))

    def test_non_integer_elements(self):
        self.assertRaises(ValueError, tuple_int_str, (('1', 'x'), ('2', 'y')))

    def test_non_string_elements(self):
        self.assertRaises(TypeError, tuple_int_str, (1, 'x'), (2, 'y'))

    def test_empty_string_elements(self):
        self.assertRaises(ValueError, tuple_int_str, (('', '2'), ('1', '')))

    def test_single_integer_element(self):
        self.assertRaises(TypeError, tuple_int_str, (('1',), ('2',)))
