import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesNumCorrespondingNum(unittest.TestCase):
    def test_typical_use_case(self):
        bases_num = [2, 3, 4]
        index = [0, 1, 2]
        expected_result = [1, 3, 16]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_edge_case_with_zero_index(self):
        bases_num = [2, 3, 4]
        index = [0, 0, 0]
        expected_result = [1, 1, 1]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_boundary_condition_with_large_numbers(self):
        bases_num = [2**64, 3**64, 4**64]
        index = [64, 64, 64]
        expected_result = [2**128, 3**128, 4**128]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_invalid_input_different_lengths(self):
        bases_num = [2, 3, 4]
        index = [0, 1]
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum(bases_num, index)

    def test_invalid_input_negative_index(self):
        bases_num = [2, 3, 4]
        index = [-1, 1, 2]
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum(bases_num, index)
