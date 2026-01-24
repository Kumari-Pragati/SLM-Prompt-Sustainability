import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCorrespondingnum(unittest.TestCase):

    def test_typical_case(self):
        bases_num = [2, 3, 4]
        index = [0, 1, 2]
        result = basesnum_coresspondingnum(bases_num, index)
        self.assertEqual(result, [1, 3, 256])

    def test_edge_case_zero_index(self):
        bases_num = [2, 3, 4]
        index = [0, 0, 0]
        result = basesnum_coresspondingnum(bases_num, index)
        self.assertEqual(result, [1, 1, 1])

    def test_boundary_case_max_limit(self):
        bases_num = [2, 3, 4]
        index = [31, 31, 31]
        result = basesnum_coresspondingnum(bases_num, index)
        self.assertEqual(result, [2147483648, 10460353203, 1073741824])

    def test_invalid_input_negative_index(self):
        bases_num = [2, 3, 4]
        index = [-1, -1, -1]
        with self.assertRaises(ValueError):
            basesnum_coresspondingnum(bases_num, index)

    def test_invalid_input_non_integer_index(self):
        bases_num = [2, 3, 4]
        index = [0.5, 1.5, 2.5]
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum(bases_num, index)
