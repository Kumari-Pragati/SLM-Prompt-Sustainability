import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):
    def test_rotate_left_typical_use_case(self):
        list1 = [1, 2, 3, 4, 5]
        m = 1
        n = 3
        expected_result = [2, 3, 4, 5, 1]
        self.assertEqual(rotate_left(list1, m, n), expected_result)

    def test_rotate_left_edge_case_m_equal_to_0(self):
        list1 = [1, 2, 3, 4, 5]
        m = 0
        n = 3
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(rotate_left(list1, m, n), expected_result)

    def test_rotate_left_edge_case_m_equal_to_length_of_list(self):
        list1 = [1, 2, 3, 4, 5]
        m = 5
        n = 3
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(rotate_left(list1, m, n), expected_result)

    def test_rotate_left_edge_case_n_equal_to_length_of_list(self):
        list1 = [1, 2, 3, 4, 5]
        m = 1
        n = 5
        expected_result = [2, 3, 4, 5, 1]
        self.assertEqual(rotate_left(list1, m, n), expected_result)

    def test_rotate_left_edge_case_m_greater_than_n(self):
        list1 = [1, 2, 3, 4, 5]
        m = 3
        n = 1
        expected_result = [3, 4, 5, 1, 2]
        self.assertEqual(rotate_left(list1, m, n), expected_result)
