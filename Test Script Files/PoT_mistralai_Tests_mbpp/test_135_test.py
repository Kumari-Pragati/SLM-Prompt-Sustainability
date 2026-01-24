import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 6)
        self.assertEqual(hexagonal_num(3), 12)
        self.assertEqual(hexagonal_num(4), 22)
        self.assertEqual(hexagonal_num(5), 30)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(hexagonal_num(0), 0)
        self.assertEqual(hexagonal_num(100), 3285)
        self.assertEqual(hexagonal_num(-1), -1)
        self.assertEqual(hexagonal_num(1000), 2979013)
