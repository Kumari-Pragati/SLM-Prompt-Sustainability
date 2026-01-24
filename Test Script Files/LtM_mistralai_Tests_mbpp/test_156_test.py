import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_simple_input(self):
        self.assertTupleEqual(tuple_int_str(('1', '2')), ((1, 2)))
        self.assertTupleEqual(tuple_int_str(('3', '4')), ((3, 4)))

    def test_edge_input(self):
        self.assertTupleEqual(tuple_int_str(('0', '0')), ((0, 0)))
        self.assertTupleEqual(tuple_int_str(('9', '9')), ((9, 9)))
        self.assertTupleEqual(tuple_int_str(('-1', '10')), ((-1, 10)))

    def test_mixed_input(self):
        self.assertTupleEqual(tuple_int_str(('1a', '2b')), ((1, 2)))
        self.assertRaises(ValueError, tuple_int_str, (('x', 'y'),))
        self.assertRaises(ValueError, tuple_int_str, (('1', 'x'),))
