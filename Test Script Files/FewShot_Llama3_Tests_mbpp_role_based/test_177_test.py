import unittest
from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(answer(1, 5), (1, 2))

    def test_valid_input2(self):
        self.assertEqual(answer(2, 10), (2, 4))

    def test_invalid_input1(self):
        self.assertEqual(answer(5, 2), -1)

    def test_invalid_input2(self):
        self.assertEqual(answer(10, 5), -1)

    def test_edge_case1(self):
        self.assertEqual(answer(0, 5), (0, 0))

    def test_edge_case2(self):
        self.assertEqual(answer(5, 5), (5, 10))
