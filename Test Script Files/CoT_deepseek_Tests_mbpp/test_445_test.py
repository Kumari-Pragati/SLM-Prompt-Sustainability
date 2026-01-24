import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):

    def test_typical_case(self):
        test_tup1 = ((1, 2, 3), (4, 5, 6))
        test_tup2 = ((7, 8, 9), (10, 11, 12))
        expected_output = ((7, 16, 27), (40, 55, 72))
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected_output = ()
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)

    def test_single_element_tuples(self):
        test_tup1 = (1,)
        test_tup2 = (2,)
        expected_output = (2,)
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)

    def test_mismatched_lengths(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5)
        with self.assertRaises(ValueError):
            index_multiplication(test_tup1, test_tup2)

    def test_negative_numbers(self):
        test_tup1 = (-1, -2, -3)
        test_tup2 = (4, 5, 6)
        expected_output = (-4, -10, -18)
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)
