import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(tuple_str_int('(1, 2, 3, 4)'), (1, 2, 3, 4))

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(tuple_str_int('(0, -1, 0, 1)'), (0, -1, 0, 1))
        self.assertListEqual(tuple_str_int('(1, 2, 3, 2147483647)'), (1, 2, 3, 2147483647))
        self.assertListEqual(tuple_str_int('(1, 2, 3, -2147483648)'), (1, 2, 3, -2147483648))
        self.assertListEqual(tuple_str_int('(1, 2, 3, 0)'), (1, 2, 3, 0))
        self.assertListEqual(tuple_str_int('(1, 2, 3, 1.5)'), TypeError)

    def test_special_and_corner_cases(self):
        self.assertListEqual(tuple_str_int('(1, 2, 3, 2, 1)'), TypeError)
        self.assertListEqual(tuple_str_int('(1, 2, 3, ...)'), TypeError)
        self.assertListEqual(tuple_str_int('(1, 2, 3, 1, 2, 3)'), TypeError)
        self.assertListEqual(tuple_str_int('(1, 2, 3, 1, 2, 3, 1, 2, 3)'), TypeError)
        self.assertListEqual(tuple_str_int('(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)'), TypeError)
        self.assertListEqual(tuple_str_int('(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)'), TypeError)
        self.assertListEqual(tuple_str_int('(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)'), TypeError)
        self.assertListEqual(tuple_str_int('(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)'), TypeError)
        self.assertListEqual(tuple_str_int('(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)'), TypeError)
        self.assertListEqual(tuple_str_int('(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)'), TypeError)
        self.assertListEqual(tuple_str_int('(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1,