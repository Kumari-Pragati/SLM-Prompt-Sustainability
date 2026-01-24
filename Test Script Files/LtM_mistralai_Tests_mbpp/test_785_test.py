import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(tuple_str_int('(1, 2, 3)'), (1, 2, 3))
        self.assertListEqual(tuple_str_int('(0, -1, 0)'), (0, -1, 0))
        self.assertListEqual(tuple_str_int('(999, 1000, 1001)'), (999, 1000, 1001))

    def test_edge_cases(self):
        self.assertListEqual(tuple_str_int('(,)'), ())
        self.assertListEqual(tuple_str_int('(1,,3)'), (1, None, 3))
        self.assertListEqual(tuple_str_int('(1,2,3,4,5)'), (1, 2, 3, 4, 5))
        self.assertListEqual(tuple_str_int('(1,2,3,4,5,)'), (1, 2, 3, 4, 5))
        self.assertListEqual(tuple_str_int('(1,2,3,4,5,6,)'), (1, 2, 3, 4, 5, 6))

    def test_special_flags(self):
        self.assertListEqual(tuple_str_int('(1,2,3,...)'), (1, 2, 3))
        self.assertListEqual(tuple_str_int('(1,2,3,...,5)'), (1, 2, 3, 4, 5))
        self.assertListEqual(tuple_str_int('(1,2,3,...,5,6)'), (1, 2, 3, 4, 5, 6))
