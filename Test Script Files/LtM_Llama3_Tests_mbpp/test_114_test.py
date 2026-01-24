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

    def test_empty_list_with_duplicates(self):
        self.assertEqual(assign_freq([1, 1, 2, 2, 2]), '[(1, 2), (2, 3)]')

    def test_list_with_negative_numbers(self):
        self.assertEqual(assign_freq([-1, -1, 0, 0, 1, 1]), '[(-1, 2), (0, 2), (1, 2)]')

    def test_list_with_zero(self):
        self.assertEqual(assign_freq([0, 0, 1, 1]), '[(0, 2), (1, 2)]')
