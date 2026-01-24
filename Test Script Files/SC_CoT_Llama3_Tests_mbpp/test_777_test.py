import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 3), 6)

    def test_edge_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 3, 4, 5], 3), 6)

    def test_edge_case2(self):
        self.assertEqual(find_Sum([1, 1, 1, 1, 1, 1], 1), 1)

    def test_edge_case3(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5, 6], 6), 21)

    def test_edge_case4(self):
        self.assertEqual(find_Sum([1, 1, 1, 1, 1, 1], 5), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Sum("hello", 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            find_Sum([1, 2, 3], "hello")

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            find_Sum(None, 3)

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            find_Sum([1, 2, 3], None)
