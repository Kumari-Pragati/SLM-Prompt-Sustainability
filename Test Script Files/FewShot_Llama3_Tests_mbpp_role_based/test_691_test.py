import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):
    def test_group_element_empty_list(self):
        self.assertEqual(group_element([]), {})

    def test_group_element_single_element(self):
        self.assertEqual(group_element([(1, 1)]), {1: [(1, 1)]})

    def test_group_element_multiple_elements(self):
        self.assertEqual(group_element([(1, 1), (2, 1), (3, 2), (4, 2)]), {1: [(1, 1), (2, 1)], 2: [(3, 2), (4, 2)]})

    def test_group_element_duplicates(self):
        self.assertEqual(group_element([(1, 1), (2, 1), (2, 1), (3, 2)]), {1: [(1, 1), (2, 1)], 2: [(3, 2)]})

    def test_group_element_sorted_list(self):
        self.assertEqual(group_element([(1, 1), (2, 1), (3, 2), (4, 2)]), {1: [(1, 1), (2, 1)], 2: [(3, 2), (4, 2)]})
