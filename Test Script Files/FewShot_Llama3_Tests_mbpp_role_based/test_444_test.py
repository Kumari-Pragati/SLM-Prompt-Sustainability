import unittest
from mbpp_444_code import trim_tuple

class TestTrimTuple(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 1
        expected_output = [(2, 3), (5, 6), (8, 9)]
        self.assertEqual(trim_tuple(test_list, K), str(expected_output))

    def test_edge_case_K_is_zero(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 0
        expected_output = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        self.assertEqual(trim_tuple(test_list, K), str(expected_output))

    def test_edge_case_K_is_equal_to_length_of_tuple(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 2
        expected_output = [(3), (6), (9)]
        self.assertEqual(trim_tuple(test_list, K), str(expected_output))

    def test_edge_case_K_is_greater_than_length_of_tuple(self):
        test_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        K = 5
        expected_output = [(), (), ()]
        self.assertEqual(trim_tuple(test_list, K), str(expected_output))
