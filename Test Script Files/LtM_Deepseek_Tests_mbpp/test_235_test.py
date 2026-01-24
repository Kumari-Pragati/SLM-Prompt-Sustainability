import unittest
from mbpp_235_code import even_bit_set_number

class TestEvenBitSetNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(even_bit_set_number(0), 0)
        self.assertEqual(even_bit_set_number(1), 3)
        self.assertEqual(even_bit_set_number(2), 2)
        self.assertEqual(even_bit_set_number(3), 3)
        self.assertEqual(even_bit_set_number(4), 4)

    def test_edge_conditions(self):
        self.assertEqual(even_bit_set_number(1023), 1023)
        self.assertEqual(even_bit_set_number(1024), 2048)
        self.assertEqual(even_bit_set_number(2048), 2048)
        self.assertEqual(even_bit_set_number(32768), 32768)
        self.assertEqual(even_bit_set_number(65535), 65535)

    def test_complex_cases(self):
        self.assertEqual(even_bit_set_number(65536), 65536)
        self.assertEqual(even_bit_set_number(131072), 131072)
        self.assertEqual(even_bit_set_number(262144), 262144)
        self.assertEqual(even_bit_set_number(524288), 524288)
        self.assertEqual(even_bit_set_number(1048576), 1048576)
