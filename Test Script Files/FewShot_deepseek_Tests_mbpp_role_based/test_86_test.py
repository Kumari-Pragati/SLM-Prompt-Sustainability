import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(centered_hexagonal_number(5), 85)

    def test_edge_condition(self):
        self.assertEqual(centered_hexagonal_number(1), 1)

    def test_boundary_condition(self):
        self.assertEqual(centered_hexagonal_number(0), 1)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            centered_hexagonal_number(-1)
