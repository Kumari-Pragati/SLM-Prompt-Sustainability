import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)
        self.assertEqual(Check_Vow("Hello", "AEIOU"), 2)
        self.assertEqual(Check_Vow("HELLO", "AEIOU"), 2)
        self.assertEqual(Check_Vow("aeiou", "aeiou"), 5)
        self.assertEqual(Check_Vow("AEIOU", "AEIOU"), 5)

    def test_edge_cases(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)
        self.assertEqual(Check_Vow("aeiou", ""), 0)
        self.assertEqual(Check_Vow("ae", "aeiou"), 1)
        self.assertEqual(Check_Vow("aeiouy", "aeiou"), 5)
        self.assertEqual(Check_Vow("aeiouAEIOU", "aeiouAEIOU"), 10)

    def test_boundary_cases(self):
        self.assertEqual(Check_Vow("a", "aeiou"), 1)
        self.assertEqual(Check_Vow("aeiou", "a"), 0)
        self.assertEqual(Check_Vow("aeiouAEIOU", "AEIOU"), 5)
        self.assertEqual(Check_Vow("AEIOU", "aeiouAEIOU"), 5)
