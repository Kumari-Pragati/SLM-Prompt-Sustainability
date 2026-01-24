import unittest
from mbpp_114_code import Counter
from 114_code import assign_freq

class TestAssignFreq(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(assign_freq([1, 2, 2, 3, 3, 3]), "((1, 1), (2, 2), (3, 3))")

    def test_empty_list(self):
        self.assertEqual(assign_freq([]), "()")

    def test_single_element_list(self):
        self.assertEqual(assign_freq([4]), "((4, 1))")

    def test_negative_numbers(self):
        self.assertEqual(assign_freq([-1, -2, -2]), "((-1, 1), (-2, 2))")

    def test_duplicate_floats(self):
        self.assertEqual(assign_freq([3.14, 3.14, 2.71]), "((2.71, 1), ((3.14, 2)))")
