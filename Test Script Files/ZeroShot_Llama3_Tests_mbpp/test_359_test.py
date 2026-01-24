import unittest
from mbpp_359_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(Check_Solution(1, 3, 2), "Yes")

    def test_negative_values(self):
        self.assertEqual(Check_Solution(-1, -3, -2), "Yes")

    def test_zero_values(self):
        self.assertEqual(Check_Solution(0, 0, 0), "Yes")

    def test_non_integer_values(self):
        self.assertEqual(Check_Solution(1.5, 3.5, 2.5), "Yes")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", "b", "c")

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 2)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            Check_Solution(1, 2, "c")
