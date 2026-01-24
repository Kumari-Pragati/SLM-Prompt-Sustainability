import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(tuple_int_str(("1", "2")), ((1, 2),))

    def test_edge_case_empty_input(self):
        self.assertEqual(tuple_int_str(()), ())

    def test_edge_case_single_element_input(self):
        self.assertEqual(tuple_int_str(("1",)), ((1,),))

    def test_edge_case_multiple_elements_input(self):
        self.assertEqual(tuple_int_str(("1", "2", "3")), ((1, 2), (2, 3)))

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            tuple_int_str([("1", "2")])

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            tuple_int_str("hello")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            tuple_int_str(None)
