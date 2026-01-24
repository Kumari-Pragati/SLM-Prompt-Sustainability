import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonalNumber(3), 15)
        self.assertEqual(centered_hexagonalNumber(4), 29)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(centered_hexagonalNumber(0), 1)
        self.assertEqual(centered_hexagonalNumber(100), 3000001)
        self.assertEqual(centered_hexagonalNumber(-1), None)
        self.assertEqual(centered_hexagonalNumber(1.5), None)
        self.assertEqual(centered_hexagonalNumber('str'), None)
