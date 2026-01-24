import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):

    def test_hexagonal_num(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 3)
        self.assertEqual(hexagonal_num(3), 6)
        self.assertEqual(hexagonal_num(4), 10)
        self.assertEqual(hexagonal_num(5), 15)
        self.assertEqual(hexagonal_num(6), 21)
        self.assertEqual(hexagonal_num(7), 28)
        self.assertEqual(hexagonal_num(8), 36)
        self.assertEqual(hexagonal_num(9), 45)
        self.assertEqual(hexagonal_num(10), 55)

    def test_hexagonal_num_edge_cases(self):
        self.assertRaises(TypeError, hexagonal_num, 'a')
        self.assertRaises(TypeError, hexagonal_num, -1)
