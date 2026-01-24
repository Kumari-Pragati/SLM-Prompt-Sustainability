import unittest
from mbpp_667_code import Check_Vow

class TestCheck_Vow(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Vow("hello", 'aeiou'), 2)

    def test_edge_case(self):
        self.assertEqual(Check_Vow("hello", 'aeiouy'), 2)

    def test_edge_case2(self):
        self.assertEqual(Check_Vow("hello", 'aeiouAEIOU'), 2)

    def test_edge_case3(self):
        self.assertEqual(Check_Vow("hello", 'AEIOU'), 0)

    def test_edge_case4(self):
        self.assertEqual(Check_Vow("", 'aeiou'), 0)

    def test_edge_case5(self):
        self.assertEqual(Check_Vow("hello", ''), 0)

    def test_edge_case6(self):
        self.assertEqual(Check_Vow("hello", 'aeiouyAEIOU'), 2)

    def test_edge_case7(self):
        self.assertEqual(Check_Vow("hello", 'AEIOUy'), 0)

    def test_edge_case8(self):
        self.assertEqual(Check_Vow("hello", 'AEIOUyAEIOU'), 0)
