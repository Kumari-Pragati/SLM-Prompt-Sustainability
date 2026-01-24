import unittest
from mbpp_715_code import str_to_tuple

class TestStrToTuple(unittest.TestCase):
    def test_simple(self):
        self.assertTupleEqual(str_to_tuple('1, 2, 3'), (1, 2, 3))
        self.assertTupleEqual(str_to_tuple('4, 5, 6'), (4, 5, 6))

    def test_edge_cases(self):
        self.assertTupleEqual(str_to_tuple(''), ())
        self.assertTupleEqual(str_to_tuple('1'), (1,))
        self.assertTupleEqual(str_to_tuple('1, 2, 3, 4, 5, 6'), (1, 2, 3, 4, 5, 6))
        self.assertTupleEqual(str_to_tuple('-1, 0, 1'), (-1, 0, 1))
        self.assertTupleEqual(str_to_tuple('1, 2, 3, 2147483647, -2147483648'), (1, 2, 2147483647, -2147483648))

    def test_complex_cases(self):
        self.assertTupleEqual(str_to_tuple('1, 2, 3, a, b'), (1, 2, 3, None, None))
        self.assertTupleEqual(str_to_tuple('1, 2, 3, 2.5, 4'), (1, 2, 3, None, 4))
        self.assertTupleEqual(str_to_tuple('"1","2","3"'), (1, 2, 3))
        self.assertTupleEqual(str_to_tuple('1, 2, 3, 1, 2, 3'), (1, 2, 3, 1, 2, 3))
