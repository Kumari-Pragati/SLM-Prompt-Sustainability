import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):

    def test_typical_case(self):
        lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_sum_list(lists), [7, 8, 9])

    def test_empty_list(self):
        lists = []
        self.assertEqual(max_sum_list(lists), [])

    def test_single_list(self):
        lists = [[1, 2, 3]]
        self.assertEqual(max_sum_list(lists), [1, 2, 3])

    def test_negative_numbers(self):
        lists = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(max_sum_list(lists), [-7, -8, -9])

    def test_equal_sums(self):
        lists = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        self.assertEqual(max_sum_list(lists), [1, 2, 3])

    def test_empty_sublists(self):
        lists = [[], [], []]
        self.assertEqual(max_sum_list(lists), [])

    def test_none_input(self):
        with self.assertRaises(TypeError):
            max_sum_list(None)
