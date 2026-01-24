import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        self.assertEqual(replace_list(list1, list2), [4, 5, 6])

    def test_edge_condition(self):
        list1 = []
        list2 = [4, 5, 6]
        self.assertEqual(replace_list(list1, list2), [4, 5, 6])

    def test_boundary_condition(self):
        list1 = [1]
        list2 = [4, 5, 6]
        self.assertEqual(replace_list(list1, list2), [4, 5, 6])

    def test_invalid_input(self):
        list1 = 'not a list'
        list2 = [4, 5, 6]
        with self.assertRaises(TypeError):
            replace_list(list1, list2)
