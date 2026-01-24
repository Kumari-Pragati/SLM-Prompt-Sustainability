import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [1, 2, 3, 4, 5]
        m = 1
        n = 3
        self.assertEqual(sum_range_list(list1, m, n), 6)

    def test_edge_condition(self):
        list1 = [1, 2, 3, 4, 5]
        m = 0
        n = 0
        self.assertEqual(sum_range_list(list1, m, n), 1)

    def test_boundary_condition(self):
        list1 = [1, 2, 3, 4, 5]
        m = 0
        n = 4
        self.assertEqual(sum_range_list(list1, m, n), 15)

    def test_invalid_input(self):
        list1 = [1, 2, 3, 4, 5]
        m = 'a'
        n = 4
        with self.assertRaises(TypeError):
            sum_range_list(list1, m, n)
