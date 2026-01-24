import unittest
from mbpp_54_code import counting_sort

class TestCountingSort(unittest.TestCase):

    def test_typical_input(self):
        my_list = [2, 4, 2, 8, 10, 3, 1]
        expected_output = [1, 2, 2, 3, 4, 8, 10]
        self.assertEqual(counting_sort(my_list), expected_output)

    def test_edge_case(self):
        my_list = [1]
        expected_output = [1]
        self.assertEqual(counting_sort(my_list), expected_output)

    def test_edge_case2(self):
        my_list = []
        expected_output = []
        self.assertEqual(counting_sort(my_list), expected_output)

    def test_edge_case3(self):
        my_list = [0]
        expected_output = [0]
        self.assertEqual(counting_sort(my_list), expected_output)

    def test_edge_case4(self):
        my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(counting_sort(my_list), expected_output)

    def test_invalid_input(self):
        my_list = 'abc'
        with self.assertRaises(TypeError):
            counting_sort(my_list)
