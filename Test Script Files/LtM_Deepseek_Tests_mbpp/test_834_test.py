import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(generate_matrix(1), [[1]])
        self.assertEqual(generate_matrix(2), [[1, 2], [4, 3]])
        self.assertEqual(generate_matrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_edge_conditions(self):
        self.assertEqual(generate_matrix(0), [])
        self.assertEqual(generate_matrix(-1), [])

    def test_complex_cases(self):
        self.assertEqual(generate_matrix(4), 
                         [[1, 2, 3, 4], 
                          [12, 13, 14, 5], 
                          [11, 16, 15, 6], 
                          [10, 9, 8, 7]])
