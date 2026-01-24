import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3, 4, 5]
        m = 1
        n = 4
        self.assertEqual(sum_range_list(list1, m, n), 9)

    def test_edge_case_m_equal_n(self):
        list1 = [1, 2, 3, 4, 5]
        m = 4
        n = 4
        self.assertEqual(sum_range_list(list1, m, n), 4)

    def test_edge_case_m_greater_than_n(self):
        list1 = [1, 2, 3, 4, 5]
        m = 5
        n = 2
        self.assertEqual(sum_range_list(list1, m, n), 3)

    def test_edge_case_m_equal_to_0(self):
        list1 = [1, 2, 3, 4, 5]
        m = 0
        n = 4
        self.assertEqual(sum_range_list(list1, m, n), 9)

    def test_edge_case_n_greater_than_list_length(self):
        list1 = [1, 2, 3, 4]
        m = 1
        n = 6
        self.assertEqual(sum_range_list(list1, m, n), 6)

    def test_invalid_input_type_m(self):
        list1 = [1, 2, 3, 4, 5]
        m = 'a'
        n = 4
        with self.assertRaises(TypeError):
            sum_range_list(list1, m, n)

    def test_invalid_input_type_n(self):
        list1 = [1, 2, 3, 4, 5]
        m = 1
        n = 'b'
        with self.assertRaises(TypeError):
            sum_range_list(list1, m, n)
