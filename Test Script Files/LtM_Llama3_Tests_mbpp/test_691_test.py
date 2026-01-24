import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(group_element([]), {})

    def test_single_element(self):
        self.assertEqual(group_element([(1, 'a')]), {(1, 'a'): ['a']})

    def test_multiple_elements(self):
        self.assertEqual(group_element([(1, 'a'), (2, 'b'), (1, 'c')]), {(1, 'a'): ['a', 'c'], (2, 'b'): ['b']})

    def test_empty_group(self):
        self.assertEqual(group_element([(1, 'a'), (2, 'b'), (3, 'c')]), {(1, 'a'): ['a'], (2, 'b'): ['b'], (3, 'c'): ['c']})

    def test_group_with_duplicates(self):
        self.assertEqual(group_element([(1, 'a'), (1, 'b'), (2, 'c')]), {(1, 'a'): ['a', 'b'], (2, 'c'): ['c']})

    def test_group_with_empty_subgroup(self):
        self.assertEqual(group_element([(1, 'a'), (1, 'b'), (1, '')]), {(1, 'a'): ['a', 'b'], (1, ''): ['', '']})

    def test_group_with_empty_subgroup_and_duplicates(self):
        self.assertEqual(group_element([(1, 'a'), (1, 'b'), (1, ''), (1, '')]), {(1, 'a'): ['a', 'b'], (1, ''): ['', '', '']})
