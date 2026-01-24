import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = ((1, 2, 3), (4, 5, 6))
        test_tup2 = ((7, 8, 9), (10, 11, 12))
        expected_output = ((7, 16, 27), (40, 55, 72))
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)

    def test_edge_conditions(self):
        test_tup1 = ((0, 0, 0), (0, 0, 0))
        test_tup2 = ((1, 1, 1), (1, 1, 1))
        expected_output = ((0, 0, 0), (0, 0, 0))
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)

    def test_boundary_conditions(self):
        test_tup1 = ((1, 2, 3), (4, 5, 6))
        test_tup2 = ((7, 8, 9), (10, 11, 12))
        expected_output = ((7, 16, 27), (40, 55, 72))
        self.assertEqual(index_multiplication(test_tup1, test_tup2), expected_output)

    def test_invalid_input(self):
        test_tup1 = ((1, 2, 3), (4, 5, 6))
        test_tup2 = ((7, 8, 9), (10, 11))  # Invalid input
        with self.assertRaises(ValueError):
            index_multiplication(test_tup1, test_tup2)
