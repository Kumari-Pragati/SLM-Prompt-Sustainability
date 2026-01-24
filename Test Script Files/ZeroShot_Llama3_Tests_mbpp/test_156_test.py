import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(tuple_int_str(("1", "2"), ("3", "4")), ((1, 2), (3, 4)))

    def test_empty_input(self):
        self.assertEqual(tuple_int_str(()), ())

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            tuple_int_str("1", "2")

    def test_single_element_input(self):
        self.assertEqual(tuple_int_str(("1",)), ((1,),))

    def test_multiple_elements_input(self):
        self.assertEqual(tuple_int_str(("1", "2", "3", "4")), ((1, 2), (3, 4)))
