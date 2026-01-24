import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(group_element([]), {})

    def test_single_element(self):
        self.assertEqual(group_element([(1, 'a')]), {(1, 'a'): ['a']})

    def test_multiple_elements(self):
        self.assertEqual(group_element([(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd')]),
                         {(1, 'a'): ['a', 'c'], (2, 'b'): ['b'], (3, 'd'): ['d']})

    def test_duplicates(self):
        self.assertEqual(group_element([(1, 'a'), (1, 'a'), (2, 'b'), (2, 'b')]),
                         {(1, 'a'): ['a', 'a'], (2, 'b'): ['b', 'b']})

    def test_sorted_list(self):
        self.assertEqual(group_element([(1, 'a'), (2, 'b'), (3, 'c')]),
                         {(1, 'a'): ['a'], (2, 'b'): ['b'], (3, 'c'): ['c']})

    def test_unsorted_list(self):
        self.assertEqual(group_element([(3, 'c'), (2, 'b'), (1, 'a')]),
                         {(1, 'a'): ['a'], (2, 'b'): ['b'], (3, 'c'): ['c']})
