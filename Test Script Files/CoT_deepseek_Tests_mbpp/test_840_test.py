import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):

    def test_b_is_zero(self):
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")

    def test_b_is_not_zero(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 0, "c")

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            Check_Solution(1, -1, 1)
