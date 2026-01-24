import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)

    def test_edge_case(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)

    def test_corner_case(self):
        self.assertEqual(Check_Vow("AEIOU", "aeiou"), 0)
        self.assertEqual(Check_Vow("bcdfghjklmnpqrstvwxyz", "aeiou"), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Check_Vow(123, "aeiou")
        with self.assertRaises(TypeError):
            Check_Vow("hello", 123)
