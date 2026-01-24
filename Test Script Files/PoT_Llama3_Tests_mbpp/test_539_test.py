import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCoresspondingnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [1, 2, 3]), [2, 9, 16])

    def test_edge_case_zero_index(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [0, 1, 2]), [1, 2, 4])

    def test_edge_case_zero_bases_num(self):
        self.assertEqual(basesnum_coresspondingnum([0, 1, 2], [1, 2, 3]), [1, 1, 1])

    def test_edge_case_negative_index(self):
        with self.assertRaises(IndexError):
            basesnum_coresspondingnum([2, 3, 4], [-1, 2, 3])

    def test_edge_case_negative_bases_num(self):
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum([-1, 1, 2], [1, 2, 3])

    def test_edge_case_empty_index(self):
        with self.assertRaises(IndexError):
            basesnum_coresspondingnum([2, 3, 4], [])

    def test_edge_case_empty_bases_num(self):
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum([], [1, 2, 3])
