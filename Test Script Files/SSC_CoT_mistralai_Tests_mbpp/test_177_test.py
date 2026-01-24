import unittest
from mbpp_177_code import answer

class TestAnswerFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(answer(1, 3), (1, 2))
        self.assertEqual(answer(5, 10), (5, 10))

    def test_edge_cases(self):
        self.assertEqual(answer(0, 1), (-1,))
        self.assertEqual(answer(1, 0), (-1,))
        self.assertEqual(answer(2, 2), (2, 4))

    def test_boundary_cases(self):
        self.assertEqual(answer(1, 2), (1, 2))
        self.assertEqual(answer(100, 101), (100, 200))

    def test_invalid_inputs(self):
        self.assertEqual(answer(-1, 1), (-1,))
        self.assertEqual(answer(1, -1), (-1,))
        self.assertEqual(answer(1.5, 2), (-1,))
        self.assertEqual(answer('a', 1), (-1,))
