import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):
    def test_typical_use_case(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        self.assertEqual(sum_list(lst1, lst2), [5, 7, 9])

    def test_edge_condition(self):
        lst1 = []
        lst2 = []
        self.assertEqual(sum_list(lst1, lst2), [])

    def test_boundary_condition(self):
        lst1 = [0]
        lst2 = [0]
        self.assertEqual(sum_list(lst1, lst2), [0])

    def test_different_lengths(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5]
        self.assertEqual(sum_list(lst1, lst2), [5, 7, 3])

    def test_negative_numbers(self):
        lst1 = [-1, -2, -3]
        lst2 = [-4, -5, -6]
        self.assertEqual(sum_list(lst1, lst2), [-5, -7, -9])

    def test_invalid_input(self):
        lst1 = [1, 2, 'a']
        lst2 = [4, 5, 6]
        with self.assertRaises(TypeError):
            sum_list(lst1, lst2)
