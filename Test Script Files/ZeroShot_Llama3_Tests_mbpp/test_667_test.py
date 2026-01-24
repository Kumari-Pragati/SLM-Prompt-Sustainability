import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):

    def test_check_vow(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)
        self.assertEqual(Check_Vow("world", "aeiou"), 2)
        self.assertEqual(Check_Vow("python", "aeiou"), 2)
        self.assertEqual(Check_Vow("abc", "aeiou"), 0)
        self.assertEqual(Check_Vow("xyz", "aeiou"), 0)
        self.assertEqual(Check_Vow("hello world", "aeiou"), 3)
        self.assertEqual(Check_Vow("aeiou", "aeiou"), 5)
        self.assertEqual(Check_Vow("AEIOU", "AEIOU"), 5)
        self.assertEqual(Check_Vow("AEIOU", "aeiou"), 3)
        self.assertEqual(Check_Vow("aeiouAEIOU", "aeiouAEIOU"), 10)
