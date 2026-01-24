import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(frequency([1, 2, 3, 2, 4], 2), 2)

    def test_empty_input(self):
        self.assertEqual(frequency([], 2), 0)

    def test_single_element_input(self):
        self.assertEqual(frequency([5], 5), 1)
        self.assertEqual(frequency([5], 6), 0)

    def test_boundary_conditions(self):
        self.assertEqual(frequency([-1, 0, 1], 0), 1)
        self.assertEqual(frequency([-1, 0, 1], -1), 1)
        self.assertEqual(frequency([-1, 0, 1], 2), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(frequency([1, 2, 2, 3, 2], 2), 3)

    def test_non_existing_element(self):
        self.assertEqual(frequency([1, 2, 3, 4, 5], 6), 0)
