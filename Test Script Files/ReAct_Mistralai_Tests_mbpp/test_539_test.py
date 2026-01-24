import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesNumCorrespondingNum(unittest.TestCase):

    def test_empty_base(self):
        self.assertRaises(ValueError, basesnum_coresspondingnum, [], 10)

    def test_single_base(self):
        self.assertEqual(basesnum_coresspondingnum([2], [10]), [2 ** 10])

    def test_multiple_bases(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 5], [2, 3, 4]),
                         [4, 81, 625])

    def test_different_lengths(self):
        self.assertRaises(ValueError, basesnum_coresspondingnum, [2, 3], [1, 2, 3])

    def test_negative_index(self):
        self.assertRaises(ValueError, basesnum_coresspondingnum, [2, 3], [-1])

    def test_zero_index(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3], [0]), [1, 1])

    def test_large_index(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3], [100]), [1048576, 536870912])
