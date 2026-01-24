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
        self.assertEqual(perfect_squares(0, 5), [])

    def test_edge_case_b_zero(self):
        self.assertEqual(perfect_squares(1, 0), [])

    def test_edge_case_a_b_equal(self):
        self.assertEqual(perfect_squares(1, 1), [1])

    def test_edge_case_a_b_negative(self):
        with self.assertRaises(ValueError):
            perfect_squares(-1, -2)

    def test_edge_case_a_b_large(self):
        self.assertEqual(perfect_squares(1, 100), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
