import unittest
from mbpp_656_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [2, 3, 4], 3), 4)

    def test_edge_case(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [1, 2, 3], 3), 0)

    def test_edge_case2(self):
        self.assertEqual(find_Min_Sum([1, 2, 3], [4, 5, 6], 3), 6)

    def test_edge_case3(self):
        self.assertEqual(find_Min_Sum([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Min_Sum("a", [1, 2, 3], 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            find_Min_Sum([1, 2, 3], "a", 3)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            find_Min_Sum([1, 2, 3], [1, 2, 3], "a")
