import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesNumCorrespondingNum(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(basesnum_coresspondingnum([], 3), [])

    def test_single_base(self):
        self.assertListEqual(basesnum_coresspondingnum([2], [3]), [8])

    def test_multiple_bases(self):
        self.assertListEqual(basesnum_coresspondingnum([2, 3, 5], [2, 3, 4]), [4, 81, 625])

    def test_different_lengths(self):
        self.assertListEqual(basesnum_coresspondingnum([2, 3], [3, 5]), [8, 243])

    def test_negative_index(self):
        self.assertRaises(IndexError, basesnum_coresspondingnum, [2, 3], [-1])
