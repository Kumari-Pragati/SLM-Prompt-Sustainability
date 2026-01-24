import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):
    def test_max_of_three_positive_numbers(self):
        self.assertEqual(max_of_three(5, 3, 1), 5)
        self.assertEqual(max_of_three(3, 5, 1), 5)
        self.assertEqual(max_of_three(3, 1, 5), 5)
        self.assertEqual(max_of_three(1, 5, 3), 5)
        self.assertEqual(max_of_three(1, 3, 5), 5)
        self.assertEqual(max_of_three(5, 1, 3), 5)

    def test_max_of_three_zero_and_positive_numbers(self):
        self.assertEqual(max_of_three(0, 5, 3), 5)
        self.assertEqual(max_of_three(5, 0, 3), 5)
        self.assertEqual(max_of_three(3, 5, 0), 5)
        self.assertEqual(max_of_three(0, 3, 5), 5)
        self.assertEqual(max_of_three(0, 3, 0), 0)
        self.assertEqual(max_of_three(3, 0, 0), 0)

    def test_max_of_three_negative_numbers(self):
        self.assertEqual(max_of_three(-5, -3, -1), -1)
        self.assertEqual(max_of_three(-3, -5, -1), -1)
        self.assertEqual(max_of_three(-3, -1, -5), -1)
        self.assertEqual(max_of_three(-1, -5, -3), -1)
        self.assertEqual(max_of_three(-1, -3, -5), -1)
        self.assertEqual(max_of_three(-5, -1, -3), -1)

    def test_max_of_three_mixed_numbers(self):
        self.assertEqual(max_of_three(-5, 3, 1), 3)
        self.assertEqual(max_of_three(3, -5, 1), 3)
        self.assertEqual(max_of_three(3, 1, -5), 3)
        self.assertEqual(max_of_three(-5, 1, 3), 3)
        self.assertEqual(max_of_three(1, -5, 3), 3)
        self.assertEqual(max_of_three(1, 3, -5), 3)
