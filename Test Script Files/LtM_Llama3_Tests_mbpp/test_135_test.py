import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 3)
        self.assertEqual(hexagonal_num(3), 7)
        self.assertEqual(hexagonal_num(4), 9)
        self.assertEqual(hexagonal_num(5), 15)

    def test_edge_cases(self):
        self.assertEqual(hexagonal_num(0), 0)
        self.assertEqual(hexagonal_num(-1), None)
        self.assertEqual(hexagonal_num(0.5), None)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            hexagonal_num('a')
        with self.assertRaises(TypeError):
            hexagonal_num(None)
