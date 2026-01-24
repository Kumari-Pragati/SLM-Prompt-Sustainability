import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(tuple_int_str([('1', '2'), ('3', '4')]), ((1, 2), (3, 4)))

    def test_edge_conditions(self):
        self.assertEqual(tuple_int_str([]), ())
        self.assertEqual(tuple_int_str([('0', '0')]), (0, 0))

    def test_boundary_conditions(self):
        self.assertEqual(tuple_int_str([('1000000000', '2000000000')]), (1000000000, 2000000000))
        self.assertEqual(tuple_int_str([('-1000000000', '-2000000000')]), (-1000000000, -2000000000))

    def test_complex_cases(self):
        self.assertEqual(tuple_int_str([('999999999', '1000000001')]), (999999999, 1000000001))
        self.assertEqual(tuple_int_str([('12345678901234567890', '98765432109876543210')]), 
                         (12345678901234567890, 98765432109876543210))
