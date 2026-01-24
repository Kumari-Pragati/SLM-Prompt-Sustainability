import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 3, 2]), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(frequency_Of_Largest(1, [5]), 1)

    def test_edge_case_all_same_elements(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 5, 5, 5, 5]), 5)

    def test_boundary_case_empty_array(self):
        self.assertEqual(frequency_Of_Largest(0, []), 0)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(frequency_Of_Largest(5, [-1, -2, -3, -3, -2]), 1)

    def test_corner_case_mixed_numbers(self):
        self.assertEqual(frequency_Of_Largest(5, [1, -2, 3, 3, -2]), 2)

    def test_corner_case_large_numbers(self):
        self.assertEqual(frequency_Of_Largest(5, [1000, 2000, 3000, 3000, 2000]), 2)
