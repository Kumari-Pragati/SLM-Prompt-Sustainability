import unittest
from mbpp_904_code import even_num

class TestEvenNum(unittest.TestCase):
    def test_even_num_positive(self):
        self.assertTrue(even_num(0))
        self.assertTrue(even_num(2))
        self.assertTrue(even_num(100))

    def test_even_num_negative(self):
        self.assertFalse(even_num(1))
        self.assertFalse(even_num(-1))
        self.assertFalse(even_num(-100))

    def test_edge_cases(self):
        self.assertTrue(even_num(2147483646))  # max int
        self.assertTrue(even_num(-2147483647))  # min int
        self.assertTrue(even_num(0.5))  # float
        self.assertTrue(even_num(-0.5))  # float
        self.assertTrue(even_num(complex(0, 0)))  # complex
