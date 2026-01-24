import unittest
from mbpp_177_code import answer

class TestAnswerFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(answer(2, 4), (2, 4))

    def test_boundary_case(self):
        self.assertEqual(answer(1, 2), (1, 2))

    def test_edge_case(self):
        self.assertEqual(answer(0, 0), (0, 0))

    def test_negative_case(self):
        self.assertEqual(answer(-1, -2), (-1, -2))

    def test_large_numbers_case(self):
        self.assertEqual(answer(1000000, 2000000), (1000000, 2000000))

    def test_L_greater_than_R(self):
        self.assertEqual(answer(3, 2), -1)

    def test_L_equals_R(self):
        self.assertEqual(answer(1, 2), -1)

    def test_L_equals_zero(self):
        self.assertEqual(answer(0, 1), -1)
