import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_duplic_list([1, 2, 3, 2, 4, 1]), [1, 2, 3, 4])
        self.assertEqual(remove_duplic_list(['a', 'b', 'c', 'a', 'd', 'b']), ['a', 'b', 'c', 'd'])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(remove_duplic_list([]), [])
        self.assertEqual(remove_duplic_list([None]), [None])
        self.assertEqual(remove_duplic_list([1, 1, 1]), [1])
        self.assertEqual(remove_duplic_list([1, 1.0, 1]), [1, 1.0])
        self.assertEqual(remove_duplic_list([1, '1', 1]), [1, '1'])

    def test_special_cases(self):
        self.assertEqual(remove_duplic_list([float('inf'), float('-inf'), 0]), [float('inf'), 0, float('-inf')])
        self.assertEqual(remove_duplic_list([1, -1, 1, -1, 0]), [1, -1, 0])
        self.assertEqual(remove_duplic_list([1, 2.0, 3.0, 2]), [1, 2.0, 3.0])
