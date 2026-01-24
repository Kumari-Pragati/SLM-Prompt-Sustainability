import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mutiple_tuple((2, 3, 4)), 24)

    def test_single_element(self):
        self.assertEqual(mutiple_tuple((5,)), 5)

    def test_empty_tuple(self):
        self.assertEqual(mutiple_tuple(()), 1)

    def test_negative_numbers(self):
        self.assertEqual(mutiple_tuple((-2, -3, -4)), -24)

    def test_zero(self):
        self.assertEqual(mutiple_tuple((2, 3, 0)), 0)

    def test_large_numbers(self):
        self.assertEqual(mutiple_tuple((1000000000, 1000000000)), 1000000000000000000)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            mutiple_tuple((2, 3, 'a'))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            mutiple_tuple([2, 3, 4])
