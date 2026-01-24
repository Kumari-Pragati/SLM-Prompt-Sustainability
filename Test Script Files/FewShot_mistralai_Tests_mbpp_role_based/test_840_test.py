import unittest
from mbpp_840_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    def test_zero_as_second_argument(self):
        self.assertEqual(Check_Solution(1, 0, 1), "Yes")

    def test_non_zero_as_second_argument(self):
        self.assertEqual(Check_Solution(1, 1, 1), "No")

    def test_negative_second_argument(self):
        self.assertEqual(Check_Solution(1, -1, 1), "No")

    def test_invalid_input_second_argument(self):
        with self.assertRaises(TypeError):
            Check_Solution(1, "not_a_number", 1)
