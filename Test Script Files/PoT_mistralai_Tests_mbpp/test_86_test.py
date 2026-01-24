import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 19)
        self.assertEqual(centered_hexagonal_number(4), 37)
        self.assertEqual(centered_hexagonal_number(5), 61)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(centered_hexagonal_number(0), 1)
        self.assertEqual(centered_hexagonal_number(100), 30001)
        self.assertEqual(centered_hexagonal_number(-1), None)
