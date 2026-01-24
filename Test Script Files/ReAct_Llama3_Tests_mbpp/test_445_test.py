import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((4, 10, 18),))

    def test_edge_case_empty_tuples(self):
        self.assertEqual(index_multiplication((), ()), ((),))

    def test_edge_case_single_element_tuples(self):
        self.assertEqual(index_multiplication((1,), (2,)), ((2,),))

    def test_edge_case_zero_length_tuples(self):
        self.assertEqual(index_multiplication([], [3, 4]), ([],))

    def test_error_case_non_tuple_input(self):
        with self.assertRaises(TypeError):
            index_multiplication(1, 2)

    def test_error_case_non_tuple_input2(self):
        with self.assertRaises(TypeError):
            index_multiplication((1, 2), '3')
