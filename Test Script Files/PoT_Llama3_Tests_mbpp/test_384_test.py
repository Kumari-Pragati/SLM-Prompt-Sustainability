import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 2, 3, 3]), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)

    def test_edge_case_all_equal(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 1, 1, 1, 1]), 5)

    def test_edge_case_all_distinct(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 4, 5]), 1)

    def test_edge_case_min_at_end(self):
        self.assertEqual(frequency_Of_Smallest(5, [5, 5, 5, 5, 1]), 1)

    def test_edge_case_min_at_start(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 4, 5]), 1)

    def test_edge_case_min_in_middle(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 1, 4, 5]), 2)

    def test_edge_case_min_at_first_and_last(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 1, 2, 3, 1]), 2)
