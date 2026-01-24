import unittest
from mbpp_156_code import tuple_int_str

class TestTupleIntStr(unittest.TestCase):

    def test_normal_input(self):
        self.assertTupleEqual(tuple_int_str(((1, 'a'), (2, 'b'))), ((1, 2),))
        self.assertTupleEqual(tuple_int_str(((3, 'c'), (4, 'd'))), ((3, 4),))

    def test_edge_input(self):
        self.assertTupleEqual(tuple_int_str(((0, 'e'),)), ((0, 0),))
        self.assertTupleEqual(tuple_int_str(((5, 'f'), (6, 'g'))), ((5, 6),))

    def test_boundary_input(self):
        self.assertTupleEqual(tuple_int_str(((-1, 'h'),)), ((-1, -1),))
        self.assertTupleEqual(tuple_int_str(((7, 'i'),)), ((7, 7),))

    def test_invalid_input(self):
        self.assertRaises(ValueError, tuple_int_str, (('x', 'y'),))
        self.assertRaises(ValueError, tuple_int_str, (('a', 1), (2, 'b'),))
