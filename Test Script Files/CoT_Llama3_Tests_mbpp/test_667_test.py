import unittest
from mbpp_667_code import Check_Vow

class TestCheck_Vow(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Check_Vow("hello", 'aeiou'), 2)

    def test_edge_case(self):
        self.assertEqual(Check_Vow("hello", 'aeiou'), 0)

    def test_edge_case2(self):
        self.assertEqual(Check_Vow("hello", 'xyz'), 0)

    def test_edge_case3(self):
        self.assertEqual(Check_Vow("", 'aeiou'), 0)

    def test_edge_case4(self):
        self.assertEqual(Check_Vow("hello", ''), 0)

    def test_edge_case5(self):
        self.assertEqual(Check_Vow("hello", None), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Check_Vow(123, 'aeiou')

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            Check_Vow("hello", 123)
