import unittest
from mbpp_316_code import find_last_occurrence

class TestFindLastOccurrence(unittest.TestCase):

    def test_typical_case(self):
        A = [1, 2, 2, 3, 4, 5, 6]
        x = 2
        self.assertEqual(find_last_occurrence(A, x), 2)

    def test_single_occurrence(self):
        A = [1, 2, 3, 4, 5, 6]
        x = 6
        self.assertEqual(find_last_occurrence(A, x), 5)

    def test_no_occurrence(self):
        A = [1, 2, 3, 4, 5, 6]
        x = 7
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_empty_list(self):
        A = []
        x = 1
        self.assertEqual(find_last_occurrence(A, x), -1)

    def test_negative_numbers(self):
        A = [-1, -2, -2, -3, -4, -5, -6]
        x = -2
        self.assertEqual(find_last_occurrence(A, x), 2)

    def test_duplicate_numbers(self):
        A = [1, 2, 2, 2, 3, 4, 5, 6]
        x = 2
        self.assertEqual(find_last_occurrence(A, x), 3)

    def test_large_numbers(self):
        A = list(range(1, 10001))
        x = 5000
        self.assertEqual(find_last_occurrence(A, x), 5000)
