import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(generate_matrix(0), [])

    def test_one_element_matrix(self):
        self.assertEqual(generate_matrix(1), [[0]])

    def test_small_matrix(self):
        expected = [[1], [2, 3], [4, 5, 6]]
        self.assertEqual(generate_matrix(3), expected)

    def test_large_matrix(self):
        expected = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
        self.assertEqual(generate_matrix(5), expected)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            generate_matrix(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            generate_matrix(3.14)
