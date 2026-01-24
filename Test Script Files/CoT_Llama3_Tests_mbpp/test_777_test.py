import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 3), 6)

    def test_edge_case(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 1), 1)

    def test_edge_case2(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case3(self):
        self.assertEqual(find_Sum([1, 2, 3, 4, 5], 0), None)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Sum("abc", 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            find_Sum([1, 2, 3], "abc")
