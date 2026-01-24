import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 2, 3, 3]), 2)

    def test_edge_case_single_element_array(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)

    def test_edge_case_empty_array(self):
        with self.assertRaises(IndexError):
            frequency_Of_Smallest(0, [])

    def test_edge_case_array_with_single_element(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)

    def test_edge_case_array_with_all_elements_equal(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 1, 1, 1, 1]), 5)

    def test_edge_case_array_with_all_elements_distinct(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 4, 5]), 1)
