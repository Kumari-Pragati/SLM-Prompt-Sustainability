import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_typical_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        leftrange = 2
        rigthrange = 8
        result = remove_list_range(list1, leftrange, rigthrange)
        self.assertEqual(result, [[4, 5, 6], [7, 8, 9]])

    def test_edge_case_leftrange_greater_than_max(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        leftrange = 10
        rigthrange = 15
        result = remove_list_range(list1, leftrange, rigthrange)
        self.assertEqual(result, [])

    def test_edge_case_rigthrange_less_than_min(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        leftrange = 0
        rigthrange = 1
        result = remove_list_range(list1, leftrange, rigthrange)
        self.assertEqual(result, [])

    def test_edge_case_leftrange_equals_rigthrange(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        leftrange = 5
        rigthrange = 5
        result = remove_list_range(list1, leftrange, rigthrange)
        self.assertEqual(result, [])

    def test_error_case_non_list_input(self):
        list1 = 12345
        leftrange = 2
        rigthrange = 8
        with self.assertRaises(TypeError):
            remove_list_range(list1, leftrange, rigthrange)

    def test_error_case_empty_list(self):
        list1 = []
        leftrange = 2
        rigthrange = 8
        result = remove_list_range(list1, leftrange, rigthrange)
        self.assertEqual(result, [])
