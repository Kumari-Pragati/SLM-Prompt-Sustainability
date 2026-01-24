import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertDictEqual(group_element([(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)]), {'1': [(1, 1), (1, 2)], '2': [(2, 1), (2, 2)], '3': [(3, 3)]})

    def test_empty_list(self):
        self.assertDictEqual(group_element([]), {})

    def test_single_element(self):
        self.assertDictEqual(group_element([(1, 1)]), {'1': [(1, 1)]})

    def test_duplicate_key(self):
        self.assertDictEqual(group_element([(1, 1), (1, 1)]), {'1': [(1, 1)]})

    def test_reverse_order(self):
        self.assertDictEqual(group_element([(2, 2), (1, 1)]), {'1': [(1, 1)], '2': [(2, 2)]})

    def test_mixed_order(self):
        self.assertDictEqual(group_element([(1, 1), (2, 2), (1, 2)]), {'1': [(1, 1), (1, 2)], '2': [(2, 2)]})
