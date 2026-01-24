import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 16)
        self.assertEqual(centered_hexagonal_number(4), 29)
        self.assertEqual(centered_hexagonal_number(5), 44)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(centered_hexagonal_number(0), 1)
        self.assertEqual(centered_hexagonal_number(-1), None)
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)

    def test_special_or_corner_cases(self):
        self.assertEqual(centered_hexagonal_number(10), 165)
        self.assertEqual(centered_hexagonal_number(20), 465)
        self.assertEqual(centered_hexagonal_number(30), 795)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number('a')
        with self.assertRaises(TypeError):
            centered_hexagonal_number(None)
