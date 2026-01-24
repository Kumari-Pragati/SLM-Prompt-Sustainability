import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 5), 3)

    def test_edge_case_zero_lens(self):
        self.assertEqual(find_remainder([], 0, 5), 1)

    def test_edge_case_one_element(self):
        self.assertEqual(find_remainder([4], 1, 5), 4)

    def test_edge_case_negative_n(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, -5), 1)

    def test_edge_case_negative_arr(self):
        self.assertEqual(find_remainder([-1, -2, -3], 3, 5), 3)
