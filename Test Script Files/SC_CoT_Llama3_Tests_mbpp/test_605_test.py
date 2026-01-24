import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):

    def test_prime_num_typical(self):
        self.assertTrue(prime_num(7))

    def test_prime_num_edge(self):
        self.assertFalse(prime_num(1))
        self.assertFalse(prime_num(4))
        self.assertTrue(prime_num(23))

    def test_prime_num_edge2(self):
        self.assertFalse(prime_num(6))
        self.assertFalse(prime_num(8))
        self.assertTrue(prime_num(11))

    def test_prime_num_edge3(self):
        self.assertFalse(prime_num(10))
        self.assertFalse(prime_num(12))
        self.assertTrue(prime_num(13))

    def test_prime_num_edge4(self):
        self.assertFalse(prime_num(14))
        self.assertFalse(prime_num(15))
        self.assertTrue(prime_num(17))

    def test_prime_num_edge5(self):
        self.assertFalse(prime_num(20))
        self.assertFalse(prime_num(21))
        self.assertTrue(prime_num(23))

    def test_prime_num_edge6(self):
        self.assertFalse(prime_num(24))
        self.assertFalse(prime_num(25))
        self.assertTrue(prime_num(29))

    def test_prime_num_edge7(self):
        self.assertFalse(prime_num(30))
        self.assertFalse(prime_num(31))
        self.assertTrue(prime_num(37))

    def test_prime_num_edge8(self):
        self.assertFalse(prime_num(40))
        self.assertFalse(prime_num(41))
        self.assertTrue(prime_num(43))

    def test_prime_num_edge9(self):
        self.assertFalse(prime_num(50))
        self.assertFalse(prime_num(51))
        self.assertTrue(prime_num(53))

    def test_prime_num_edge10(self):
        self.assertFalse(prime_num(60))
        self.assertFalse(prime_num(61))
        self.assertTrue(prime_num(67))

    def test_prime_num_invalid(self):
        with self.assertRaises(TypeError):
            prime_num('a')
