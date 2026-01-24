import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(hexagonal_num(5), 15)

    def test_boundary_conditions(self):
        self.assertEqual(hexagonal_num(0), 0)
        self.assertEqual(hexagonal_num(1), 1)

    def test_large_number(self):
        self.assertEqual(hexagonal_num(100), 19900)

    def test_negative_number(self):
        self.assertEqual(hexagonal_num(-5), -15)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            hexagonal_num('a')
