import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)

    def test_edge_case(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)

    def test_boundary_case(self):
        self.assertEqual(Check_Vow("aeiou", "aeiou"), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Check_Vow(12345, "aeiou")
