import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):

    def test_even_num_simple(self):
        self.assertTrue(even_num(2))
        self.assertTrue(even_num(0))

    def test_even_num_edge(self):
        self.assertFalse(even_num(1))
        self.assertFalse(even_num(-1))

    def test_even_num_boundary(self):
        self.assertTrue(even_num(2**31))
        self.assertFalse(even_num(2**31 - 1))

    def test_even_num_complex(self):
        self.assertTrue(even_num(2**62))
        self.assertFalse(even_num(2**63 - 1))
