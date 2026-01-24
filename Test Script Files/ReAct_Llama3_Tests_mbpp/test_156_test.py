import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_int_str(("1", "2")), ((1, 2),))

    def test_edge_case_empty(self):
        self.assertEqual(tuple_int_str(()), ())

    def test_edge_case_single_element(self):
        self.assertEqual(tuple_int_str(("3",)), ((3,),))

    def test_edge_case_multiple_elements(self):
        self.assertEqual(tuple_int_str(("4", "5", "6")), ((4, 5), (5, 6)))

    def test_error_case_non_integer(self):
        with self.assertRaises(ValueError):
            tuple_int_str(("a", "b"))

    def test_error_case_non_string(self):
        with self.assertRaises(TypeError):
            tuple_int_str((1, 2))
