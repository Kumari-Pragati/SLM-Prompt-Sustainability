import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):

    def test_func(self):
        self.assertEqual(func([[1, 1], [2, 2], [3, 3]], 2), [1, 2])
        self.assertEqual(func([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 3), [1, 2, 3])
        self.assertEqual(func([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]], 4, ), [1, 2, 3, 4])
        self.assertEqual(func([[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]], 5), [1, 2, 3, 4, 5])
        self.assertEqual(func([[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3]], 6), [1, 2, 3, 4, 5, 6])
        self.assertEqual(func([[1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3]], 7), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(func([[1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3]], 8), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(func([[1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3]], 9), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(func([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]], 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_func_empty_input(self):
        self.assertEqual(func([], 2), [])

    def test_func_empty_input_and_k(self):
        self.assertEqual(func([], 0), [])

    def test_func_empty_input_and_k_zero(self):
        self.assertEqual(func([], 0), [])

    def test_func_empty_input_and_k_negative(self):
        with self.assertRaises(ValueError):
            func([], -1)

    def test_func_empty_input_and_k_negative_zero(self):
        with self.assertRaises(ValueError):
            func([], 0)
