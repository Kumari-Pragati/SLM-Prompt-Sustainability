import unittest
from mbpp_880_code import Check_Solution

class Test_Check_Solution(unittest.TestCase):
    def test_simple_valid(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No solutions")
    def test_simple_valid2(self):
        self.assertEqual(Check_Solution(1, 0, 1), "1 solution")
    def test_simple_valid3(self):
        self.assertEqual(Check_Solution(1, 4, 1), "2 solutions")
    def test_edge_case1(self):
        self.assertEqual(Check_Solution(1, 0, 0), "1 solution")
    def test_edge_case2(self):
        self.assertEqual(Check_Solution(0, 0, 0), "No solutions")
    def test_edge_case3(self):
        self.assertEqual(Check_Solution(1, 2, 0), "2 solutions")
    def test_edge_case4(self):
        self.assertEqual(Check_Solution(1, 0, 0), "1 solution")
    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 2, 3)
    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 3)
    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            Check_Solution(1, 2, "c")
