import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)
        self.assertEqual(Check_Vow("world", "aeiou"), 1)

    def test_edge_conditions(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)
        self.assertEqual(Check_Vow("AEIOU", "aeiou"), 0)
        self.assertEqual(Check_Vow("AEIOU", ""), 0)

    def test_boundary_conditions(self):
        self.assertEqual(Check_Vow("a"*21, "aeiou"), 21)
        self.assertEqual(Check_Vow("a"*22, "aeiou"), 21)

    def test_complex_cases(self):
        self.assertEqual(Check_Vow("AEIOU", "AEIOU"), 5)
        self.assertEqual(Check_Vow("AEIOUaeiou", "AEIOU"), 5)
        self.assertEqual(Check_Vow("AEIOUaeiou", "aeiou"), 10)
