import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):

    def test_typical_case(self):
        n = 3
        expected_output = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(generate_matrix(n), expected_output)

    def test_edge_case_n_equals_1(self):
        n = 1
        expected_output = [[1]]
        self.assertEqual(generate_matrix(n), expected_output)

    def test_edge_case_n_equals_0(self):
        n = 0
        expected_output = []
        self.assertEqual(generate_matrix(n), expected_output)

    def test_negative_n(self):
        n = -3
        expected_output = []
        self.assertEqual(generate_matrix(n), expected_output)

    def test_large_n(self):
        n = 10
        # This test may take a while to run due to the large size of the matrix
        self.assertIsNotNone(generate_matrix(n))
