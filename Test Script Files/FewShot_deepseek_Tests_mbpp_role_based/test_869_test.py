import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        leftrange = 2
        rigthrange = 8
        self.assertEqual(remove_list_range(list1, leftrange, rigthrange), [[2, 3], [5, 6], [8, 9]])

    def test_edge_condition(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        leftrange = 1
        rigthrange = 1
        self.assertEqual(remove_list_range(list1, leftrange, rigthrange), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_boundary_condition(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        leftrange = 2
        rigthrange = 2
        self.assertEqual(remove_list_range(list1, leftrange, rigthrange), [])

    def test_invalid_input(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        leftrange = 'a'
        rigthrange = 2
        with self.assertRaises(TypeError):
            remove_list_range(list1, leftrange, rigthrange)
