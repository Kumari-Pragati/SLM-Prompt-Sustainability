import unittest
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(assign_freq([]), '[]')

    def test_single_element_list(self):
        self.assertEqual(assign_freq([1]), '[(1, 1)]')

    def test_multiple_elements_list(self):
        self.assertEqual(assign_freq([1, 2, 2, 3, 3, 3]), '[(1, 1), (2, 2), (3, 3)]')

    def test_duplicates(self):
        self.assertEqual(assign_freq([1, 1, 2, 2, 2, 3, 3, 3, 3]), '[(1, 2), (2, 3), (3, 4)]')

    def test_non_integer_values(self):
        self.assertEqual(assign_freq(['a', 'a', 'b', 'c', 'c']), '[(\'a\', 2), (\'b\', 1), (\'c\', 2)]')

    def test_empty_string(self):
        self.assertEqual(assign_freq(['']), '[]')

    def test_string_values(self):
        self.assertEqual(assign_freq(['a', 'b', 'c', 'c']), '[(\'a\', 1), (\'b\', 1), (\'c\', 2)]')
