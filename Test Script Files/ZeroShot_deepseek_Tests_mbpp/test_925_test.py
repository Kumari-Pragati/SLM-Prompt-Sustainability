import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(mutiple_tuple((2, 3, 4)), 24)

    def test_negative_numbers(self):
        self.assertEqual(mutiple_tuple((-2, -3, -4)), -24)

    def test_mixed_numbers(self):
        self.assertEqual(mutiple_tuple((2, -3, 4)), -24)

    def test_single_number(self):
        self.assertEqual(mutiple_tuple((5,)), 5)

    def test_empty_tuple(self):
        self.assertEqual(mutiple_tuple(()), 1)
