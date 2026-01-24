import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 6)
        self.assertEqual(hexagonal_num(3), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(hexagonal_num(0), 0)
        self.assertEqual(hexagonal_num(100), 3285)
        self.assertEqual(hexagonal_num(-1), -1)
