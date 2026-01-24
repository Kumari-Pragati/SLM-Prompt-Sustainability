import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 9)
        self.assertEqual(hexagonal_num(3), 20)

    def test_edge_cases(self):
        self.assertEqual(hexagonal_num(0), 0)
        self.assertEqual(hexagonal_num(10), 99)

    def test_corner_cases(self):
        self.assertEqual(hexagonal_num(-1), -2)
        self.assertEqual(hexagonal_num(-10), -99)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            hexagonal_num("1")
        with self.assertRaises(TypeError):
            hexagonal_num(None)
