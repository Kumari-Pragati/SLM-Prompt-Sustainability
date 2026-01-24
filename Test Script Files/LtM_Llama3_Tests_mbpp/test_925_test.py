import unittest
from mbpp_925_code import mutiple_tuple

class TestMutipleTuple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(mutiple_tuple((1, 2, 3)), 6)
    def test_empty(self):
        self.assertEqual(mutiple_tuple(()), 1)
    def test_single(self):
        self.assertEqual(mutiple_tuple((5,)), 5)
    def test_negative(self):
        self.assertEqual(mutiple_tuple((-1, 2, 3)), -6)
    def test_zero(self):
        self.assertEqual(mutiple_tuple((0, 2, 3)), 0)
    def test_max(self):
        self.assertEqual(mutiple_tuple((2**31 - 1,)), 2**31 - 1)
    def test_min(self):
        self.assertEqual(mutiple_tuple((-2**31,)), -2**31)
