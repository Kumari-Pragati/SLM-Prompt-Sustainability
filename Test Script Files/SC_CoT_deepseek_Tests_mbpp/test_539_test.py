import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesNumCorrespondingNum(unittest.TestCase):

    def test_typical_case(self):
        bases_num = [2, 3, 4]
        index = [0, 1, 2]
        expected_result = [1, 3, 16]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_edge_case_zero_index(self):
        bases_num = [2, 3, 4]
        index = [0, 0, 0]
        expected_result = [1, 1, 1]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_edge_case_single_element(self):
        bases_num = [2]
        index = [0]
        expected_result = [1]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_boundary_case_large_numbers(self):
        bases_num = [1000, 2000]
        index = [2, 3]
        expected_result = [1000000, 8000000]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), expected_result)

    def test_invalid_input_different_lengths(self):
        bases_num = [2, 3, 4]
        index = [0, 1]
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum(bases_num, index)

    def test_invalid_input_negative_index(self):
        bases_num = [2, 3, 4]
        index = [-1, 0, 1]
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum(bases_num, index)
