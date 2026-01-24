import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(hexagonal_num(3), 10)
        self.assertEqual(hexagonal_num(4), 20)
        self.assertEqual(hexagonal_num(5), 35)

    def test_edge_cases(self):
        self.assertEqual(hexagonal_num(0), 0)
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 6)

    def test_negative_input(self):
        self.assertRaises(ValueError, hexagonal_num, -1)

    def test_fractional_input(self):
        self.assertRaises(TypeError, hexagonal_num, 2.5)

    def test_string_input(self):
        self.assertRaises(TypeError, hexagonal_num, 'a')
