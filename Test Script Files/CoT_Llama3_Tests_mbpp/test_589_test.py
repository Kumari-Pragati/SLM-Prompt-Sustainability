import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])

    def test_edge_case_a_zero(self):
        self.assertEqual(perfect_squares(0, 10), [])

    def test_edge_case_b_zero(self):
        self.assertEqual(perfect_squares(1, 0), [])

    def test_edge_case_a_equal_b(self):
        self.assertEqual(perfect_squares(1, 1), [1])

    def test_edge_case_a_greater_b(self):
        self.assertEqual(perfect_squares(5, 3), [])

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            perfect_squares('a', 10)

    def test_edge_case_invalid_input2(self):
        with self.assertRaises(TypeError):
            perfect_squares(1, 'b')

    def test_edge_case_invalid_input3(self):
        with self.assertRaises(TypeError):
            perfect_squares('a', 'b')
