import unittest
from mbpp_840_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):
    def test_valid_input_yes(self):
        self.assertEqual(Check_Solution(1, 0, 2), "Yes")

    def test_valid_input_no(self):
        self.assertEqual(Check_Solution(1, 1, 2), "No")

    def test_zero_b(self):
        self.assertEqual(Check_Solution(1, 0, 2), "Yes")

    def test_non_zero_b(self):
        self.assertEqual(Check_Solution(1, 1, 2), "No")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 0, 2)
