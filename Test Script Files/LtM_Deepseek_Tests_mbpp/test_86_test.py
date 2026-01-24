import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 19)

    def test_edge_conditions(self):
        self.assertEqual(centered_hexagonal_number(0), 1)
        self.assertEqual(centered_hexagonal_number(-1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(centered_hexagonal_number(100), 5959)

    def test_complex_cases(self):
        self.assertEqual(centered_hexagonal_number(1000), 5995001)
