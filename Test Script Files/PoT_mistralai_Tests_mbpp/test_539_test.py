import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesNumCorrespondingNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(basesnum_coresspondingnum([2, 3, 5], [2, 3, 4]), [4, 27, 625])

    def test_edge_case_zero_index(self):
        self.assertListEqual(basesnum_coresspondingnum([2, 3, 5], []), [1, 1, 1])

    def test_edge_case_negative_index(self):
        self.assertListEqual(basesnum_coresspondingnum([2, 3, 5], [-1, -2, -3]), [1/2, 1/9, 1/243])

    def test_edge_case_empty_bases_num(self):
        self.assertListEqual(basesnum_coresspondingnum([], [2, 3, 4]), [])

    def test_edge_case_non_integer_index(self):
        self.assertListEqual(basesnum_coresspondingnum([2, 3, 5], [2.0, 3.0, 4.0]), [4.0, 27.0, 625.0])

    def test_edge_case_non_integer_base(self):
        self.assertListEqual(basesnum_coresspondingnum([2.0, 3.0, 5.0], [2, 3, 4]), [4.0, 27.0, 625.0])
