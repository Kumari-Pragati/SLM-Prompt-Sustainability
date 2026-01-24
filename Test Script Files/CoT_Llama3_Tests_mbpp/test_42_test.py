import unittest
from mbpp_42_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(find_Sum([1, 2, 2, 3, 4, 4, 5, 6, 6], 7), 6)

    def test_edge(self):
        self.assertEqual(find_Sum([1, 1, 1, 1], 4), 1)

    def test_empty(self):
        self.assertEqual(find_Sum([], 0), 0)

    def test_single(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Sum("hello", 7)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            find_Sum([1, 2, 3], "hello")
