import unittest
from mbpp_690_code import range
from six.moves import zip

from _690_code import mul_consecutive_nums

class TestMulConsecutiveNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(mul_consecutive_nums([1, 2, 3, 4, 5]), [2*1, 3*2, 4*3, 5*4])

    def test_edge_case_empty_list(self):
        self.assertListEqual(mul_consecutive_nums([]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(mul_consecutive_nums([1]), [])

    def test_edge_case_two_elements(self):
        self.assertListEqual(mul_consecutive_nums([1, 2]), [2])

    def test_boundary_case_first_element_zero(self):
        self.assertListEqual(mul_consecutive_nums([0, 1, 2, 3, 4]), [0, 1*2, 2*3, 3*4])

    def test_boundary_case_last_element_zero(self):
        self.assertListEqual(mul_consecutive_nums([1, 2, 3, 0, 4]), [1*2, 2*3, 0])
