import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesNumCorrespondingNum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [0, 1, 2]), [1, 3, 256])

    def test_negative_numbers(self):
        self.assertEqual(basesnum_coresspondingnum([-2, -3, -4], [0, 1, 2]), [-1, -3, -256])

    def test_zero_in_bases_num(self):
        self.assertEqual(basesnum_coresspondingnum([0, 3, 4], [0, 1, 2]), [0, 3, 256])

    def test_zero_in_index(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [0, 0, 0]), [1, 1, 1])

    def test_large_numbers(self):
        self.assertEqual(basesnum_coresspondingnum([1000, 2000, 3000], [1, 2, 3]), [1000, 4000000, 2700000000000])

    def test_empty_list(self):
        self.assertEqual(basesnum_coresspondingnum([], []), [])
