import unittest
from mbpp_539_code import basesnum_coresspondingnum

class TestBasesNumCorrespondingNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [1, 2, 3]), [2, 9, 16])

    def test_edge_case_power_of_0(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [0, 0, 0]), [1, 1, 1])

    def test_edge_case_power_of_negative(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [-1, -2, -3]), [0.5, 0.25, 0.125])

    def test_edge_case_power_of_large(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [100, 200, 300]), [1.2676536201758794e+30, 5.151825639132813e+47, 1.3440000000000002e+59])

    def test_edge_case_power_of_zero(self):
        self.assertEqual(basesnum_coresspondingnum([2, 3, 4], [0, 0, 0]), [1, 1, 1])

    def test_error_case_non_integer_input(self):
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum([2, 3, 4], ['a', 'b', 'c'])

    def test_error_case_non_list_input(self):
        with self.assertRaises(TypeError):
            basesnum_coresspondingnum('a', [1, 2, 3])
