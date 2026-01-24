import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(even_bit_set_number(10), 22)
        self.assertEqual(even_bit_set_number(20), 62)
        self.assertEqual(even_bit_set_number(42), 106)

    def test_edge_cases(self):
        self.assertEqual(even_bit_set_number(0), 1)
        self.assertEqual(even_bit_set_number(1), 3)
        self.assertEqual(even_bit_set_number(2), 3)
        self.assertEqual(even_bit_set_number(3), 5)
        self.assertEqual(even_bit_set_number(4), 6)
        self.assertEqual(even_bit_set_number(5), 7)
        self.assertEqual(even_bit_set_number(6), 6)
        self.assertEqual(even_bit_set_number(7), 9)
        self.assertEqual(even_bit_set_number(8), 10)
        self.assertEqual(even_bit_set_number(9), 11)
        self.assertEqual(even_bit_set_number(10), 12)
        self.assertEqual(even_bit_set_number(11), 13)
        self.assertEqual(even_bit_set_number(12), 12)
        self.assertEqual(even_bit_set_number(13), 15)
        self.assertEqual(even_bit_set_number(14), 16)
        self.assertEqual(even_bit_set_number(15), 17)
        self.assertEqual(even_bit_set_number(16), 16)
        self.assertEqual(even_bit_set_number(17), 19)
        self.assertEqual(even_bit_set_number(18), 20)
        self.assertEqual(even_bit_set_number(19), 21)
        self.assertEqual(even_bit_set_number(20), 22)
        self.assertEqual(even_bit_set_number(21), 23)
        self.assertEqual(even_bit_set_number(22), 22)
        self.assertEqual(even_bit_set_number(23), 25)
        self.assertEqual(even_bit_set_number(24), 26)
        self.assertEqual(even_bit_set_number(25), 27)
        self.assertEqual(even_bit_set_number(26), 26)
        self.assertEqual(even_bit_set_number(27), 29)
        self.assertEqual(even_bit_set_number(28), 30)
        self.assertEqual(even_bit_set_number(29), 31)
        self.assertEqual(even_bit_set_number(30), 30)
        self.assertEqual(even_bit_set_number(31), 33)
