import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_typical_case(self):
        test_tup1 = ((1, 2, 3), (4, 5, 6))
        test_tup2 = ((7, 8, 9), (10, 11, 12))
        expected_output = ((7, 16, 27), (40, 55, 72))
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)

    def test_edge_case_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected_output = ()
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)

    def test_boundary_case_single_element_tuples(self):
        test_tup1 = (1,)
        test_tup2 = (2,)
        expected_output = (2,)
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)

    def test_corner_case_one_empty_tuple(self):
        test_tup1 = ((1, 2, 3), ())
        test_tup2 = ((4, 5, 6), (7, 8, 9))
        expected_output = ((4, 10, 18), ())
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)

    def test_invalid_input(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5, 6, 7)
        with self.assertRaises(ValueError):
            index_multiplication(test_tup1, test_tup2)
