import unittest
from mbpp_840_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(Check_Solution(1, 0, 3), "Yes")

    def test_edge_case_b_zero(self):
        self.assertEqual(Check_Solution(1, 0, 3), "Yes")

    def test_edge_case_b_nonzero(self):
        self.assertEqual(Check_Solution(1, 1, 3), "No")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 0, 3)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 3)
