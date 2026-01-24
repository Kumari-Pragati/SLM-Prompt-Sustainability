import unittest
from mbpp_925_code import mutiple_tuple

class TestMutipleTuple(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(mutiple_tuple((1, 2, 3, 4)), 24)

    def test_zero_in_list(self):
        self.assertEqual(mutiple_tuple((1, 0, 3, 4)), 0)

    def test_negative_numbers(self):
        self.assertEqual(mutiple_tuple((-1, -2, -3, -4)), 80)

    def test_empty_list(self):
        self.assertEqual(mutiple_tuple(()), 1)

    def test_single_number(self):
        self.assertEqual(mutiple_tuple((5,)), 5)

    def test_single_zero(self):
        self.assertEqual(mutiple_tuple((0,)), 0)
