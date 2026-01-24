import unittest
from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(answer(3, 6), (3, 6))

    def test_edge_case_L_greater_than_R(self):
        self.assertEqual(answer(4, 3), -1)

    def test_boundary_case_L_equals_R(self):
        self.assertEqual(answer(4, 4), (4, 8))

    def test_boundary_case_L_equals_zero(self):
        self.assertEqual(answer(0, 0), (0, 0))

    def test_invalid_input_L_negative(self):
        with self.assertRaises(TypeError):
            answer(-1, 2)

    def test_invalid_input_R_negative(self):
        with self.assertRaises(TypeError):
            answer(1, -2)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            answer(1.5, 2)
