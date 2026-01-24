import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mutiple_tuple([]), 1)

    def test_single_element_list(self):
        self.assertEqual(mutiple_tuple([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(mutiple_tuple([1, 2, 3, 4, 5]), 120)

    def test_negative_numbers(self):
        self.assertEqual(mutiple_tuple([-1, -2, -3, -4, -5]), 120)

    def test_mixed_numbers(self):
        self.assertEqual(mutiple_tuple([1, -2, 3, -4, 5]), -120)

    def test_zero(self):
        self.assertEqual(mutiple_tuple([0]), 0)
