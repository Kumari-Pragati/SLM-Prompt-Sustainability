import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 3)
        self.assertEqual(hexagonal_num(3), 7)
        self.assertEqual(hexagonal_num(4), 9)
        self.assertEqual(hexagonal_num(5), 15)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(hexagonal_num(0), 0)
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(-1), None)
        self.assertEqual(hexagonal_num(0.5), None)

    def test_corner_cases(self):
        self.assertEqual(hexagonal_num(10), 55)
        self.assertEqual(hexagonal_num(100), 9901)
