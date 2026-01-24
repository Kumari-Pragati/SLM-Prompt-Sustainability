import unittest
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(assign_freq([1, 2, 2, 3, 3, 3]), 
                         "[(1, 1), (2, 2), (3, 3)]")

    def test_empty_input(self):
        self.assertEqual(assign_freq([]), 
                         "[]")

    def test_single_element_input(self):
        self.assertEqual(assign_freq([1]), 
                         "[(1, 1)]")

    def test_duplicate_elements(self):
        self.assertEqual(assign_freq([1, 1, 1, 2, 2, 3]), 
                         "[(1, 3), (2, 2), (3, 1)]")

    def test_negative_numbers(self):
        self.assertEqual(assign_freq([-1, -1, 2, 2, -3, -3, -3]), 
                         "[(-1, 2), (2, 2), (-3, 3)]")

    def test_mixed_numbers(self):
        self.assertEqual(assign_freq([1, -1, 2, -2, 3, -3]), 
                         "[(-3, 1), (-2, 1), (-1, 1), (1, 1), (2, 1), (3, 1)]")
