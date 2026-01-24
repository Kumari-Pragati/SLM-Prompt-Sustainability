import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):
    def test_remove_list_range_typical_use_case(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        leftrange = 3
        rigthrange = 7
        result = remove_list_range(list1, leftrange, rigthrange)
        self.assertEqual(result, [3, 4, 5, 6, 7])

    def test_remove_list_range_edge_case_left_range_zero(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        leftrange = 0
        rigthrange = 7
        result = remove_list_range(list1, leftrange, rigthrange)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])

    def test_remove_list_range_edge_case_right_range_max(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        leftrange = 3
        rigthrange = 10
        result = remove_list_range(list1, leftrange, rigthrange)
        self.assertEqual(result, [3, 4, 5, 6, 7, 8, 9, 10])

    def test_remove_list_range_edge_case_left_and_right_range_zero(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        leftrange = 0
        rigthrange = 10
        result = remove_list_range(list1, leftrange, rigthrange)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_remove_list_range_invalid_input_type(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        leftrange = 'a'
        rigthrange = 7
        with self.assertRaises(TypeError):
            remove_list_range(list1, leftrange, rigthrange)
