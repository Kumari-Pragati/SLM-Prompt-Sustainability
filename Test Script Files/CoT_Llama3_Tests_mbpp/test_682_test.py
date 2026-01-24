import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mul_list([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_edge_case_empty_list(self):
        self.assertEqual(mul_list([], [1, 2, 3]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(mul_list([5], [6]), [30])

    def test_edge_case_single_element_list_empty(self):
        self.assertEqual(mul_list([5], []), [])

    def test_edge_case_empty_list_empty(self):
        self.assertEqual(mul_list([], []), [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            mul_list('a', [1, 2, 3])

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            mul_list([1, 2, 3], 'a')

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            mul_list('a', 'b')
