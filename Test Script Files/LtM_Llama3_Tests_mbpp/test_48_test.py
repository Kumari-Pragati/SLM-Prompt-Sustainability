import unittest
from mbpp_48_code import odd_bit_set_number

class TestOddBitSetNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(odd_bit_set_number(5), 5)
        self.assertEqual(odd_bit_set_number(10), 10)
        self.assertEqual(odd_bit_set_number(15), 15)

    def test_edge(self):
        self.assertEqual(odd_bit_set_number(0), 0)
        self.assertEqual(odd_bit_set_number(1), 1)
        self.assertEqual(odd_bit_set_number(2**31 - 1), 2**31 - 1)

    def test_bit_set(self):
        self.assertEqual(odd_bit_set_number(3), 3)
        self.assertEqual(odd_bit_set_number(7), 7)
        self.assertEqual(odd_bit_set_number(15), 15)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_bit_set_number('a')
