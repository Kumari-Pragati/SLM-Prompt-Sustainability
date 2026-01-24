import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):
    def test_typical_cases(self):
        self.assertListEqual(tuple_str_int('(1, 2, 3)'), (1, 2, 3))
        self.assertListEqual(tuple_str_int('(0, 0, 0)'), (0, 0, 0))
        self.assertListEqual(tuple_str_int('(99, 99, 99)'), (99, 99, 99))

    def test_edge_and_boundary_cases(self):
        self.assertListEqual(tuple_str_int('(0)'), (0,))
        self.assertListEqual(tuple_str_int('(1,)'), (1,))
        self.assertListEqual(tuple_str_int('(1, 2, 3, 4)'), (1, 2, 3, 4))
        self.assertListEqual(tuple_str_int('(1, 2, 3, 4, 5)'), (1, 2, 3, 4, 5))
        self.assertListEqual(tuple_str_int('(1, 2, 3, 4, 5, 6)'), (1, 2, 3, 4, 5, 6))
        self.assertListEqual(tuple_str_int('(1, 2, 3, 4, 5, 6, 7)'), (1, 2, 3, 4, 5, 6, 7))
        self.assertListEqual(tuple_str_int('(1, 2, 3, 4, 5, 6, 7, 8)'), (1, 2, 3, 4, 5, 6, 7, 8))
        self.assertListEqual(tuple_str_int('(1, 2, 3, 4, 5, 6, 7, 8, 9)'), (1, 2, 3, 4, 5, 6, 7, 8, 9))
        self.assertListEqual(tuple_str_int('(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)'), (1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
