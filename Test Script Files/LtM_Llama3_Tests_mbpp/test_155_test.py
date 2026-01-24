import unittest
from mbpp_155_code import even_bit_toggle_number

class TestEvenBitToggleNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(even_bit_toggle_number(0), 0)
        self.assertEqual(even_bit_toggle_number(1), 1)
        self.assertEqual(even_bit_toggle_number(2), 3)
        self.assertEqual(even_bit_toggle_number(3), 1)
        self.assertEqual(even_bit_toggle_number(4), 4)
        self.assertEqual(even_bit_toggle_number(5), 5)

    def test_edge(self):
        self.assertEqual(even_bit_toggle_number(2**31 - 1), 2**31 - 1)
        self.assertEqual(even_bit_toggle_number(-2**31), -2**31)
        self.assertEqual(even_bit_toggle_number(2**31), 2**31)

    def test_complex(self):
        self.assertEqual(even_bit_toggle_number(123456789), 123456790)
        self.assertEqual(even_bit_toggle_number(987654321), 987654322)
        self.assertEqual(even_bit_toggle_number(1234567890), 1234567891)
