import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):

    def test_find_sum(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 3), 6)
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 1), 1)
        self.assertEqual(find_Sum([1, 1, 1, 1, 1], 5, ), 1)
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 0), None)
        self.assertEqual(find_Sum([], 3), None)
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], -1), None)

    def test_find_sum_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Sum("hello", 3)
        with self.assertRaises(TypeError):
            find_Sum([1, 2, 3], "hello")
        with self.assertRaises(TypeError):
            find_Sum([1, 2, 3], None)
