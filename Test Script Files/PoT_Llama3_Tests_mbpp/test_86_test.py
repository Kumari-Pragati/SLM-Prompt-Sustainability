import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 16)
        self.assertEqual(centered_hexagonal_number(4), 28)
        self.assertEqual(centered_hexagonal_number(5), 44)

    def test_edge_case(self):
        self.assertEqual(centered_hexagonal_number(0), 1)
        self.assertEqual(centered_hexagonal_number(-1), None)

    def test_boundary_case(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 16)
        self.assertEqual(centered_hexagonal_number(4), 28)
        self.assertEqual(centered_hexagonal_number(5), 44)
