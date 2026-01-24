import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTupleEqual(tuple_int_str(('1', '2')), ((1, 2)))
        self.assertTupleEqual(tuple_int_str(('3', '4')), ((3, 4)))
        self.assertTupleEqual(tuple_int_str(('5', '6')), ((5, 6)))

    def test_edge_and_boundary_cases(self):
        self.assertTupleEqual(tuple_int_str(('0', '9')), ((0, 9)))
        self.assertTupleEqual(tuple_int_str(('-1', '10')), ((-1, 10)))
        self.assertTupleEqual(tuple_int_str(('11', '20')), ((11, 20)))
        self.assertTupleEqual(tuple_int_str(('-20', '-10')), ((-20, -10)))
        self.assertTupleEqual(tuple_int_str(('', '')), ())
        self.assertTupleEqual(tuple_int_str(('', '1')), ((0, 1)))
        self.assertTupleEqual(tuple_int_str(('1', '')), ((1, 0)))
