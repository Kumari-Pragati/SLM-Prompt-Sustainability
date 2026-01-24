import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):

    def test_normal_input(self):
        self.assertDictEqual(group_element([(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)]), {'1': [(1, 1), (1, 2)], '2': [(2, 1), (2, 2)], '3': [(3, 3)]})

    def test_edge_and_boundary_conditions(self):
        self.assertDictEqual(group_element([(1, 1), (1, 1), (2, 1), (2, 2), (3, 3), (2, 2)]), {'1': [(1, 1)], '2': [(2, 1), (2, 2)], '3': [(3, 3)]})
        self.assertDictEqual(group_element([(1, 1), (1, 1), (1, 2)]), {'1': [(1, 1), (1, 1)], '2': [(1, 2)]})
        self.assertDictEqual(group_element([(1, 1), (1, 1), (1, 1), (2, 1), (2, 2), (3, 3), (2, 2)]), {'1': [(1, 1), (1, 1), (1, 1)], '2': [(2, 1), (2, 2)], '3': [(3, 3)]})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            group_element([1, 2, 3])
        with self.assertRaises(TypeError):
            group_element([(1,), (2, 2)])
