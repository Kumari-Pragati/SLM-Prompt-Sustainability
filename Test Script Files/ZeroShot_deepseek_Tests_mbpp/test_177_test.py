import unittest
from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(answer(1, 2), (1, 2))
        self.assertEqual(answer(2, 4), (2, 4))
        self.assertEqual(answer(3, 6), (3, 6))

    def test_invalid_input(self):
        self.assertEqual(answer(3, 2), -1)
        self.assertEqual(answer(5, 10), -1)
        self.assertEqual(answer(7, 14), -1)

    def test_edge_cases(self):
        self.assertEqual(answer(0, 0), (0, 0))
        self.assertEqual(answer(1, 1), (1, 2))
