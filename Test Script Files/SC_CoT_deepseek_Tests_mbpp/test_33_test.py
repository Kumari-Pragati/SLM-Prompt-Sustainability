import unittest

from mbpp_33_code import decimal_To_Binary

class TestDecimalToBinary(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(decimal_To_Binary(10), 1010)

    def test_boundary_case(self):
        self.assertEqual(decimal_To_Binary(0), 0)

    def test_edge_case(self):
        self.assertEqual(decimal_To_Binary(1), 1)
        self.assertEqual(decimal_To_Binary(2), 10)
        self.assertEqual(decimal_To_Binary(3), 11)
        self.assertEqual(decimal_To_Binary(4), 100)
        self.assertEqual(decimal_To_Binary(8), 1000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decimal_To_Binary('a')
        with self.assertRaises(TypeError):
            decimal_To_Binary(None)
        with self.assertRaises(TypeError):
            decimal_To_Binary([1, 2, 3])
        with self.assertRaises(TypeError):
            decimal_To_Binary({'key': 'value'})
