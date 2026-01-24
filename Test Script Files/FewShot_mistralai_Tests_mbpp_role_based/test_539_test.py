import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCorrespondingNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 5], [2, 3, 4]), [4, 27, 625])

    def test_zero_index(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 5], [0]), [1])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            basesnum_coresspondingnum([2, 3, 5], [-1])

    def test_empty_bases_num(self):
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum([], [1])

    def test_empty_index(self):
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum([2, 3, 5], [])
