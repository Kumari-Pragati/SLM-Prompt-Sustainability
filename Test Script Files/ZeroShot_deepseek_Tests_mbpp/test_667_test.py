import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):

    def test_Check_Vow(self):
        self.assertEqual(Check_Vow('hello', 'aeiou'), 2)
        self.assertEqual(Check_Vow('world', 'aeiou'), 1)
        self.assertEqual(Check_Vow('python', 'aeiou'), 1)
        self.assertEqual(Check_Vow('unittesting', 'aeiou'), 4)
        self.assertEqual(Check_Vow('code', 'aeiou'), 0)
