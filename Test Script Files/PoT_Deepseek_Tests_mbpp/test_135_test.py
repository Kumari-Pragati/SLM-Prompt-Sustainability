import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 9)
        self.assertEqual(hexagonal_num(3), 20)
        self.assertEqual(hexagonal_num(4), 34)
        self.assertEqual(hexagonal_num(5), 51)

    def test_edge_cases(self):
        self.assertEqual(hexagonal_num(0), 0)
        self.assertEqual(hexagonal_num(-1), -1)

    def test_boundary_cases(self):
        self.assertEqual(hexagonal_num(100), 1980)
        self.assertEqual(hexagonal_num(1000), 199980)
