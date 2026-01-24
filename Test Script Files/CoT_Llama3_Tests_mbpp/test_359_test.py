import unittest
from mbpp_359_code import Check_Solution

class TestCheck_Solution(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, 2, 3), "Yes")

    def test_edge_case_a_zero(self):
        self.assertEqual(Check_Solution(0, 2, 3), "No")

    def test_edge_case_b_zero(self):
        self.assertEqual(Check_Solution(1, 0, 3), "No")

    def test_edge_case_c_zero(self):
        self.assertEqual(Check_Solution(1, 2, 0), "No")

    def test_edge_case_a_c_zero(self):
        self.assertEqual(Check_Solution(0, 2, 3), "No")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", 2, 3)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            Check_Solution(1, "b", 3)

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            Check_Solution(1, 2, "c")
