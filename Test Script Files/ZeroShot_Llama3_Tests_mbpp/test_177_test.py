import unittest
from mbpp_177_code import answer

class TestAnswerFunction(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(answer(5, 10), (5, 10))
        self.assertEqual(answer(10, 20), (10, 20))
        self.assertEqual(answer(20, 30), (20, 30))

    def test_invalid_input(self):
        self.assertEqual(answer(5, 3), (-1))
        self.assertEqual(answer(10, 5), (-1))
        self.assertEqual(answer(20, 15), (-1))

    def test_edge_cases(self):
        self.assertEqual(answer(0, 0), (-1))
        self.assertEqual(answer(0, 1), (-1))
        self.assertEqual(answer(1, 1), (-1))
