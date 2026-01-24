import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 16)
        self.assertEqual(centered_hexagonal_number(4), 29)
        self.assertEqual(centered_hexagonal_number(5), 44)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(centered_hexagonal_number(0), 1)
        self.assertEqual(centered_hexagonal_number(-1), None)
        self.assertEqual(centered_hexagonal_number(1e10), 3 * 1e10 * (1e10 - 1) + 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number('a')
        with self.assertRaises(TypeError):
            centered_hexagonal_number(None)
