import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(perfect_squares(0, 0), [])

    def test_single_element(self):
        self.assertEqual(perfect_squares(1, 1), [1])

    def test_multiple_elements(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])

    def test_edge_case_a_zero(self):
        self.assertEqual(perfect_squares(0, 10), [1, 4, 9])

    def test_edge_case_b_zero(self):
        self.assertEqual(perfect_squares(1, 0), [])

    def test_edge_case_a_greater_than_b(self):
        self.assertEqual(perfect_squares(10, 5), [1, 4, 9])

    def test_edge_case_b_greater_than_a(self):
        self.assertEqual(perfect_squares(5, 10), [1, 4, 9, 16, 25])
