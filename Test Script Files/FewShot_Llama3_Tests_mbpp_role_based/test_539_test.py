import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesnumCoresspondingnum(unittest.TestCase):
    def test_typical_use_case(self):
        bases_num = [2, 3, 4]
        index = [1, 2, 3]
        result = [2**1, 3**2, 4**3]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), result)

    def test_edge_case_zero_index(self):
        bases_num = [2, 3, 4]
        index = [0, 0, 0]
        result = [1, 1, 1]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), result)

    def test_edge_case_negative_index(self):
        bases_num = [2, 3, 4]
        index = [-1, -2, -3]
        result = [1/2, 1/3, 1/4]
        self.assertEqual(basesnum_coresspondingnum(bases_num, index), result)

    def test_invalid_input_type(self):
        bases_num = "abc"
        index = [1, 2, 3]
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum(bases_num, index)
