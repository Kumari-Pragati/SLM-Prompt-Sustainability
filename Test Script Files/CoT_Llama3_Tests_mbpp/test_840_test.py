import unittest
from mbpp_840_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 0, 3), "Yes")

    def test_edge_case(self):
        self.assertEqual(Check_Solution(1, 1, 3), "No")

    def test_edge_case2(self):
        self.assertEqual(Check_Solution(1, 0, 0), "Yes")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 0, 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 3)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            Check_Solution(1, 0, "c")
