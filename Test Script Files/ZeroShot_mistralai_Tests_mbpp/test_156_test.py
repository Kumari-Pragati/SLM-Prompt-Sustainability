import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsInstance(tuple_int_str(()), tuple)
        self.assertEqual(tuple_int_str(()), ())

    def test_single_element_tuple(self):
        self.assertIsInstance(tuple_int_str(('1', '2')), tuple)
        self.assertEqual(tuple_int_str(('1', '2')), (1, 2))

    def test_multiple_elements_tuple(self):
        self.assertIsInstance(tuple_int_str(('3', '4'), ('5', '6'), ('7', '8'))), tuple)
        self.assertEqual(tuple_int_str(('3', '4'), ('5', '6'), ('7', '8')), (3, 4), (5, 6), (7, 8))

    def test_invalid_input(self):
        self.assertRaises(ValueError, tuple_int_str, ('1', '2', '3'))
        self.assertRaises(ValueError, tuple_int_str, (('1', '2'),))
        self.assertRaises(ValueError, tuple_int_str, (('1',), ('2',)))
