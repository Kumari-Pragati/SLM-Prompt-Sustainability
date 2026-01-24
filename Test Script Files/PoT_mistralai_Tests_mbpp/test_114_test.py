import unittest
from mbpp_114_code import Counter
from 114_code import assign_freq

class TestAssignFreq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(assign_freq([1, 2, 2, 3, 3, 3]), '(1, 1), (2, 2), (3, 3)')

    def test_edge_case_single_element(self):
        self.assertEqual(assign_freq([1]), '(1, 1)')

    def test_edge_case_empty_list(self):
        self.assertEqual(assign_freq([]), '')

    def test_corner_case_duplicate_key_and_value(self):
        self.assertEqual(assign_freq([1, 1, 2, 2, 2, 2]), '(1, 1), (2, 4)')
