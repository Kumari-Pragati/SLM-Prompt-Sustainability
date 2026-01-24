import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(generate_matrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_edge_case_n_1(self):
        self.assertEqual(generate_matrix(1), [[1]])

    def test_edge_case_n_2(self):
        self.assertEqual(generate_matrix(2), [[1, 2], [4, 3]])

    def test_edge_case_n_0(self):
        self.assertEqual(generate_matrix(0), [])

    def test_edge_case_n_negative(self):
        with self.assertRaises(ValueError):
            generate_matrix(-1)

    def test_edge_case_n_non_integer(self):
        with self.assertRaises(TypeError):
            generate_matrix('a')
