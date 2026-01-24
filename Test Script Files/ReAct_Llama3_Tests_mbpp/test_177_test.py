import unittest
from mbpp_177_code import answer

class TestAnswerFunction(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(answer(5, 10), (5, 10))

    def test_edge_case_L_equals_R(self):
        self.assertEqual(answer(5, 5), (5, 10))

    def test_edge_case_L_greater_than_R(self):
        self.assertEqual(answer(10, 5), (-1))

    def test_edge_case_L_zero(self):
        self.assertEqual(answer(0, 10), (0, 0))

    def test_edge_case_R_zero(self):
        self.assertEqual(answer(5, 0), (-1))

    def test_error_case_L_negative(self):
        with self.assertRaises(TypeError):
            answer(-5, 10)

    def test_error_case_R_negative(self):
        with self.assertRaises(TypeError):
            answer(5, -10)
