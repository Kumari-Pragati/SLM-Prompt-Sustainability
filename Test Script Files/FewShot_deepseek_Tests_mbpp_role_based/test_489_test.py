import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 3, 4]), 1)

    def test_edge_case_with_single_element(self):
        self.assertEqual(frequency_Of_Largest(1, [5]), 1)

    def test_boundary_case_with_same_elements(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 5, 5, 5, 5]), 5)

    def test_invalid_input_with_empty_array(self):
        with self.assertRaises(IndexError):
            frequency_Of_Largest(0, [])

    def test_invalid_input_with_negative_numbers(self):
        self.assertEqual(frequency_Of_Largest(5, [-1, -2, -3, -3, -4]), 1)
