import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(tuple_int_str([('1', '2'), ('3', '4')]), ((1, 2), (3, 4)))

    def test_edge_condition(self):
        self.assertEqual(tuple_int_str([('0', '0')]), ((0, 0),))

    def test_boundary_condition(self):
        self.assertEqual(tuple_int_str([('1000000000', '1000000000')]), ((1000000000, 1000000000),))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            tuple_int_str([('1', 'two'), ('3', '4')])
