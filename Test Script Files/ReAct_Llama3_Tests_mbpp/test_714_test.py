import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(count_Fac(0), 0)

    def test_one(self):
        self.assertEqual(count_Fac(1), 0)

    def test_prime(self):
        self.assertEqual(count_Fac(2), 1)

    def test_composite(self):
        self.assertEqual(count_Fac(4), 2)

    def test_large(self):
        self.assertEqual(count_Fac(100), 2)

    def test_edge_case(self):
        self.assertEqual(count_Fac(1), 0)

    def test_edge_case2(self):
        self.assertEqual(count_Fac(2), 1)
