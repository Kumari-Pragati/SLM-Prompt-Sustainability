import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 4, 5]), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)

    def test_edge_case_all_same_elements(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 1, 1, 1, 1]), 5)

    def test_edge_case_empty_array(self):
        with self.assertRaises(IndexError):
            frequency_Of_Smallest(0, [])

    def test_typical_case_with_duplicates(self):
        self.assertEqual(frequency_Of_Smallest(6, [5, 2, 3, 4, 1, 1]), 2)

    def test_edge_case_smallest_at_end(self):
        self.assertEqual(frequency_Of_Smallest(5, [2, 3, 4, 5, 1]), 1)
