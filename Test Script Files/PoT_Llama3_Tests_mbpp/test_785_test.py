import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(tuple_str_int("1,2,3"), (1, 2, 3))

    def test_edge1(self):
        self.assertEqual(tuple_str_int("1,2,3,"), (1, 2, 3))

    def test_edge2(self):
        self.assertEqual(tuple_str_int("1,2,3,4"), (1, 2, 3, 4))

    def test_edge3(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5"), (1, 2, 3, 4, 5))

    def test_edge4(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6"), (1, 2, 3, 4, 5, 6))

    def test_edge5(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7"), (1, 2, 3, 4, 5, 6, 7))

    def test_edge6(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7,8"), (1, 2, 3, 4, 5, 6, 7, 8))

    def test_edge7(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7,8,9"), (1, 2, 3, 4, 5, 6, 7, 8, 9))

    def test_edge8(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7,8,9,10"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    def test_edge9(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7,8,9,10,11"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))

    def test_edge10(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7,8,9,10,11,12"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

    def test_edge11(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7,8,9,10,11,12,13"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))

    def test_edge12(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7,8,9,10,11,12,13,14"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))

    def test_edge13(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

    def test_edge14(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))

    def test_edge15(self):
        self.assertEqual(tuple_str_int("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))

    def test_edge16(self):
        self.assertEqual(tuple_str_int("