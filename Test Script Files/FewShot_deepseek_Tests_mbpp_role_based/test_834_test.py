import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):
    def test_typical_use_case(self):
        n = 3
        expected_output = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(generate_matrix(n), expected_output)

    def test_edge_condition(self):
        n = 1
        expected_output = [[1]]
        self.assertEqual(generate_matrix(n), expected_output)

    def test_boundary_condition(self):
        n = 2
        expected_output = [[1, 2], [4, 3]]
        self.assertEqual(generate_matrix(n), expected_output)

    def test_zero_input(self):
        n = 0
        expected_output = []
        self.assertEqual(generate_matrix(n), expected_output)

    def test_negative_input(self):
        n = -1
        expected_output = []
        self.assertEqual(generate_matrix(n), expected_output)
