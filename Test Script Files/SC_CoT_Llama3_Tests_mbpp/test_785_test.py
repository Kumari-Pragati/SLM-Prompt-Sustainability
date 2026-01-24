import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(tuple_str_int("1,2,3"), (1, 2, 3))

    def test_edge_case(self):
        self.assertEqual(tuple_str_int("(1,2,3)"), (1, 2, 3))

    def test_edge_case2(self):
        self.assertEqual(tuple_str_int("1,2,3..."), (1, 2, 3))

    def test_edge_case3(self):
        self.assertEqual(tuple_str_int("...1,2,3..."), (1, 2, 3))

    def test_edge_case4(self):
        self.assertEqual(tuple_str_int("1,2,3,..."), (1, 2, 3))

    def test_edge_case5(self):
        self.assertEqual(tuple_str_int("1,2,3,..."), (1, 2, 3))

    def test_edge_case6(self):
        self.assertEqual(tuple_str_int("1,2,3,...,"), (1, 2, 3))

    def test_edge_case7(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4"), (1, 2, 3, 4))

    def test_edge_case8(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5"), (1, 2, 3, 4, 5))

    def test_edge_case9(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5,6"), (1, 2, 3, 4, 5, 6))

    def test_edge_case10(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5,6,7"), (1, 2, 3, 4, 5, 6, 7))

    def test_edge_case11(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5,6,7,8"), (1, 2, 3, 4, 5, 6, 7, 8))

    def test_edge_case12(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5,6,7,8,9"), (1, 2, 3, 4, 5, 6, 7, 8, 9))

    def test_edge_case13(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5,6,7,8,9,10"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    def test_edge_case14(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5,6,7,8,9,10,11"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))

    def test_edge_case15(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5,6,7,8,9,10,11,12"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

    def test_edge_case16(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5,6,7,8,9,10,11,12,13"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))

    def test_edge_case17(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5,6,7,8,9,10,11,12,13,14"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))

    def test_edge_case18(self):
        self.assertEqual(tuple_str_int("1,2,3,...,4,5,6,7,8,9,10,11,12,13,14,15"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

    def test_edge_case19(self):
        self.assertEqual