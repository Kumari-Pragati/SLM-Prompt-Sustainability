import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):

    def test_simple(self):
        self.assertDictEqual(group_element([(1, 1), (2, 2), (1, 1), (2, 2), (3, 3)]), {'1': [(1, 1), (1, 1)], '2': [(2, 2), (2, 2)], '3': [(3, 3)]})

    def test_edge_cases(self):
        self.assertDictEqual(group_element([(1, 1), (2, 2)]), {'1': [(1, 1)], '2': [(2, 2)]})
        self.assertDictEqual(group_element([(1, 1), (1, 1), (1, 1)]), {'1': [(1, 1), (1, 1), (1, 1)]})
        self.assertDictEqual(group_element([(1, 1), (2, 2), (3, 3), (2, 2)]), {'1': [(1, 1)], '2': [(2, 2), (2, 2)], '3': [(3, 3)]})

    def test_complex(self):
        self.assertDictEqual(group_element([(1, 1), (2, 2), (1, 1), (2, 2), (3, 3), (2, 2), (1, 1)]), {'1': [(1, 1), (1, 1)], '2': [(2, 2), (2, 2), (2, 2)], '3': [(3, 3)]})
