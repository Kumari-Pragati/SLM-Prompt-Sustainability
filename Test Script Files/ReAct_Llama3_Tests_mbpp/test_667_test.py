import unittest
from mbpp_667_code import Check_Vow

class TestCheck_Vow(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Vow("hello", 'aeiou'), 2)

    def test_edge_case1(self):
        self.assertEqual(Check_Vow("xyz", 'aeiou'), 0)

    def test_edge_case2(self):
        self.assertEqual(Check_Vow("aeiou", 'aeiou'), 5)

    def test_edge_case3(self):
        self.assertEqual(Check_Vow("", 'aeiou'), 0)

    def test_edge_case4(self):
        self.assertEqual(Check_Vow("abc", 'xyz'), 0)

    def test_edge_case5(self):
        self.assertEqual(Check_Vow("aeiou", 'xyz'), 0)

    def test_error_case1(self):
        with self.assertRaises(TypeError):
            Check_Vow(123, 'aeiou')

    def test_error_case2(self):
        with self.assertRaises(TypeError):
            Check_Vow("hello", 123)
