import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesNumCorrespondingNum(unittest.TestCase):

    def test_typical_case(self):
        bases_num = [2, 3, 4]
        index = [0, 1, 2]
        expected_result = [1, 3, 16]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_edge_case_zero_bases_num(self):
        bases_num = [0, 3, 4]
        index = [0, 1, 2]
        expected_result = [1, 3, 16]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_edge_case_negative_bases_num(self):
        bases_num = [-2, 3, 4]
        index = [0, 1, 2]
        expected_result = [1, 3, 16]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_edge_case_zero_index(self):
        bases_num = [2, 3, 4]
        index = [0, 0, 0]
        expected_result = [1, 1, 1]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_edge_case_negative_index(self):
        bases_num = [2, 3, 4]
        index = [-1, -1, -1]
        expected_result = [0.5, 0.3333333333333333, 0.25]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_error_case_different_lengths(self):
        bases_num = [2, 3, 4]
        index = [0, 1]
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum(bases_num, index)
