import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 1, 2, 3]), 1)
        self.assertEqual(frequency_Of_Smallest(3, [1, 2, 3]), 1)
        self.assertEqual(frequency_Of_Smallest(3, [3, 3, 3]), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(frequency_Of_Smallest(0, []), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(frequency_Of_Smallest(3, [-1, -1, 0]), 2)
        self.assertEqual(frequency_Of_Smallest(3, [-1, 0, 1]), 1)

    def test_corner_case_duplicate_minimum(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 1, 1]), 1)
