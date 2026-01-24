import unittest
from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(answer(1, 2), (1, 2))

    def test_edge_case_L_greater_than_R(self):
        self.assertEqual(answer(2, 1), -1)

    def test_boundary_case_L_equals_R(self):
        self.assertEqual(answer(1, 1), -1)

    def test_edge_case_L_is_zero(self):
        self.assertEqual(answer(0, 1), (0, 0))

    def test_edge_case_R_is_zero(self):
        self.assertEqual(answer(1, 0), -1)

    def test_edge_case_L_and_R_are_zero(self):
        self.assertEqual(answer(0, 0), (0, 0))

    def test_complex_case_L_is_half_of_R(self):
        self.assertEqual(answer(1, 2), (1, 2))

    def test_complex_case_L_is_greater_than_half_of_R(self):
        self.assertEqual(answer(3, 6), (-1))
