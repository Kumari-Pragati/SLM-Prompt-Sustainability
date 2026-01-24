import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCorrespondingnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [1, 2, 3]), [2, 9, 64])

    def test_single_element_list(self):
        self.assertEqual(basesnum_coresspondingnum([2], [1]), [2])

    def test_empty_list(self):
        self.assertEqual(basesnum_coresspondingnum([], []), [])

    def test_negative_bases_num(self):
        self.assertEqual(basesnum_coresspondingnum([-2, 3, 4], [1, 2, 3]), [-2, 9, 64])

    def test_zero_in_bases_num(self):
        self.assertEqual(basesnum_coresspondingnum([0, 3, 4], [1, 2, 3]), [0, 9, 64])

    def test_zero_in_index(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [0, 0, 0]), [1, 1, 1])

    def test_negative_index(self):
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum([2, 3, 4], [-1, 2, 3])

    def test_non_integer_index(self):
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum([2, 3, 4], [1.5, 2, 3])
