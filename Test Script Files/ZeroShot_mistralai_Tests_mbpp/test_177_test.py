import unittest
from mbpp_177_code import answer

class TestAnswerFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(answer([]), (-1))

    def test_single_element(self):
        self.assertEqual(answer([1]), (-1))
        self.assertEqual(answer([5]), (-1))

    def test_positive_numbers(self):
        self.assertEqual(answer([1, 2, 3, 4, 5]), (1, 2))
        self.assertEqual(answer([10, 20, 30, 40, 50]), (10, 20))

    def test_negative_numbers(self):
        self.assertEqual(answer([-1, -2, -3, -4, -5]), (-1, -2))
        self.assertEqual(answer([-10, -20, -30, -40, -50]), (-10, -20))

    def test_mixed_numbers(self):
        self.assertEqual(answer([1, -2, 3, -4, 5]), (1, 2))
        self.assertEqual(answer([-1, 2, -3, 4, -5]), (-1, 2))
