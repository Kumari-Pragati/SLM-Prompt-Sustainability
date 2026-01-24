import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_empty_input(self):
        self.assertEqual(concatenate_tuple(()), '')

    def test_single_element_input(self):
        self.assertEqual(concatenate_tuple((1,)), '1')

    def test_edge_case_input(self):
        self.assertEqual(concatenate_tuple((1, 2, 3, 4, 5)), '1-2-3-4-5')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate_tuple('hello')

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            concatenate_tuple((1, 'hello', 3))

    def test_negative_numbers_input(self):
        self.assertEqual(concatenate_tuple((-1, -2, -3)), '-1--2--3')

    def test_zero_input(self):
        self.assertEqual(concatenate_tuple((0,)), '0')

    def test_large_input(self):
        test_tup = tuple(range(1, 100))
        self.assertEqual(concatenate_tuple(test_tup), '-'.join(map(str, test_tup)))
