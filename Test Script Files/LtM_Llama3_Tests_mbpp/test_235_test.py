import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(even_bit_set_number(0), 0)
        self.assertEqual(even_bit_set_number(1), 1)
        self.assertEqual(even_bit_set_number(2), 3)
        self.assertEqual(even_bit_set_number(3), 3)
        self.assertEqual(even_bit_set_number(4), 7)
        self.assertEqual(even_bit_set_number(5), 5)

    def test_edge(self):
        self.assertEqual(even_bit_set_number(2**31 - 1), 2**31 - 1)
        self.assertEqual(even_bit_set_number(-1), -1)
        self.assertEqual(even_bit_set_number(0), 0)

    def test_complex(self):
        self.assertEqual(even_bit_set_number(2**31 - 2), 2**31 - 2)
        self.assertEqual(even_bit_set_number(2**31 - 3), 2**31 - 3)
        self.assertEqual(even_bit_set_number(2**31 - 4), 2**31 - 4)
