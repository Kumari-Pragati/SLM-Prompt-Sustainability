import unittest
from mbpp_925_code import mutiple_tuple

class TestMutipleTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(mutiple_tuple((2, 3, 4)), 24)

    def test_single_element(self):
        self.assertEqual(mutiple_tuple((5,)), 5)

    def test_empty_tuple(self):
        self.assertEqual(mutiple_tuple(()), 1)

    def test_negative_numbers(self):
        self.assertEqual(mutiple_tuple((-2, -3, -4)), -24)

    def test_zero(self):
        self.assertEqual(mutiple_tuple((2, 3, 0, 4)), 0)

    def test_float_numbers(self):
        self.assertAlmostEqual(mutiple_tuple((1.5, 2.0, 3.0)), 9.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            mutiple_tuple("not a tuple")
