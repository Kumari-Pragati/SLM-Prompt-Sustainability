import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):
    def test_single_element_array(self):
        self.assertEqual(frequency_Of_Largest(1, [1]), 1)

    def test_empty_array(self):
        self.assertEqual(frequency_Of_Largest(0, []), 0)

    def test_array_with_one_unique_element(self):
        self.assertEqual(frequency_Of_Largest(1, [1]), 1)

    def test_array_with_multiple_unique_elements(self):
        self.assertEqual(frequency_Of_Largest(2, [1, 2, 3]), 1)

    def test_array_with_duplicates(self):
        self.assertEqual(frequency_Of_Largest(3, [1, 1, 2, 1]), 2)

    def test_array_with_largest_element_at_beginning(self):
        self.assertEqual(frequency_Of_Largest(2, [5, 4, 5]), 1)

    def test_array_with_largest_element_at_end(self):
        self.assertEqual(frequency_Of_Largest(2, [4, 5, 5]), 1)

    def test_array_with_largest_element_in_middle(self):
        self.assertEqual(frequency_Of_Largest(3, [4, 5, 4, 5]), 1)

    def test_array_with_multiple_largest_elements(self):
        self.assertEqual(frequency_Of_Largest(2, [5, 5, 4]), 1)
