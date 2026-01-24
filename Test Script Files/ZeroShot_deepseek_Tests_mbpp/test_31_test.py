import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):

    def test_func(self):
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 2), [3, 2])
        self.assertEqual(func([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 1), [1])
        self.assertEqual(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), [9, 8, 7])
        self.assertEqual(func([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 3), [3, 2, 1])
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 1), [5])
        self.assertEqual(func([], 0), [])
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 6), [5, 4, 3, 2, 1])
