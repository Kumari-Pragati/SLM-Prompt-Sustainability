import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 19)
        self.assertEqual(centered_hexagonal_number(4), 37)

    def test_edge_cases(self):
        self.assertEqual(centered_hexagonal_number(0), 1)
        self.assertEqual(centered_hexagonal_number(-1), 1)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number('a')
        with self.assertRaises(ValueError):
            centered_hexagonal_number(-2)
