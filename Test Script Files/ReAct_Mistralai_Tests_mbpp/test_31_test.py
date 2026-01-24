import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(func([], 0), [])

    def test_single_list(self):
        self.assertListEqual(func([[1], [2], [3]], 1), [1, 2, 3])
        self.assertListEqual(func([[1], [2], [3]], 2), [2, 1, 3])
        self.assertListEqual(func([[1], [2], [3]], 3), [3, 1, 2])

    def test_multiple_lists(self):
        self.assertListEqual(func([[1, 2], [3, 4], [5, 6]], 2), [2, 1, 4, 3])
        self.assertListEqual(func([[1, 2], [3, 4], [5, 6]], 3), [4, 1, 2, 3])
        self.assertListEqual(func([[1, 2], [3, 4], [5, 6]], 4), [5, 1, 2, 3, 4])

    def test_duplicates(self):
        self.assertListEqual(func([[1, 1], [2, 2], [3, 3]], 2), [1, 2, 3])
        self.assertListEqual(func([[1, 1], [2, 2], [3, 3]], 3), [1, 2, 3])

    def test_k_greater_than_len(self):
        self.assertListEqual(func([[1], [2], [3]], 4), [1, 2, 3])

    def test_k_less_than_len(self):
        self.assertListEqual(func([[1], [2], [3]], 0), [])

    def test_negative_numbers(self):
        self.assertListEqual(func([[-1], [2], [-3]], 1), [2, -1, -3])

    def test_empty_numbers(self):
        self.assertListEqual(func([[], [2], []], 1), [2])
