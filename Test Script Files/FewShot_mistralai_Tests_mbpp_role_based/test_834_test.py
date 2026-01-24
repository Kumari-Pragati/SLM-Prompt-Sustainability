import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(generate_matrix(0), [])

    def test_1x1_matrix(self):
        self.assertEqual(generate_matrix(1), [[0]])

    def test_2x2_matrix(self):
        self.assertEqual(generate_matrix(2), [[0, 1], [0, 2]])

    def test_3x3_matrix(self):
        self.assertEqual(generate_matrix(3), [[0, 1, 2], [3, 4, 5], [6, 7, 8]])

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            generate_matrix(-1)
