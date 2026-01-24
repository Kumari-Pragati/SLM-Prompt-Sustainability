import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):
    def test_centered_hexagonal_number(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 18)
        self.assertEqual(centered_hexagonal_number(4), 36)
        self.assertEqual(centered_hexagonal_number(5), 63)
        self.assertEqual(centered_hexagonal_number(6), 99)
        self.assertEqual(centered_hexagonal_number(7), 135)
        self.assertEqual(centered_hexagonal_number(8), 176)
        self.assertEqual(centered_hexagonal_number(9), 224)
        self.assertEqual(centered_hexagonal_number(10), 273)

    def test_edge_cases(self):
        self.assertEqual(centered_hexagonal_number(0), 1)
        self.assertEqual(centered_hexagonal_number(-1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number('a')
        with self.assertRaises(TypeError):
            centered_hexagonal_number(None)
