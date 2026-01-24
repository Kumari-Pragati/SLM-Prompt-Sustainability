import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(big_sum([1, 2, 3]), 4)

    def test_edge_case_max_min_equal(self):
        self.assertEqual(big_sum([1, 1]), 2)

    def test_edge_case_max_min_diff(self):
        self.assertEqual(big_sum([-1, 10]), 9)

    def test_edge_case_single_element(self):
        self.assertEqual(big_sum([5]), 5)

    def test_edge_case_empty_list(self):
        with self.assertRaises(TypeError):
            big_sum([])

    def test_edge_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            big_sum(['a', 'b'])
