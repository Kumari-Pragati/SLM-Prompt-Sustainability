import unittest
from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(answer(1, 3), (1, 2))

    def test_edge_case_L_equal_R(self):
        self.assertEqual(answer(2, 4), (2, 4))

    def test_edge_case_L_greater_than_R(self):
        self.assertEqual(answer(3, 2), (-1))

    def test_edge_case_L_equal_zero(self):
        self.assertEqual(answer(0, 1), (-1))

    def test_edge_case_R_equal_zero(self):
        self.assertEqual(answer(1, 0), (-1))

    def test_edge_case_L_and_R_equal_zero(self):
        self.assertEqual(answer(0, 0), (-1))
