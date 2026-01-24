import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 19)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(centered_hexagonal_number(0), 1)
        self.assertEqual(centered_hexagonal_number(-1), None)
        self.assertEqual(centered_hexagonal_number(1e9), None)

    def test_complex_scenarios(self):
        self.assertEqual(centered_hexagonal_number(100), 30003)
        self.assertEqual(centered_hexagonal_number(1000), 3000003)
