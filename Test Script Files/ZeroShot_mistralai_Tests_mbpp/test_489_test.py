import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(frequency_Of_Largest(0, []), 0)

    def test_single_element(self):
        self.assertEqual(frequency_Of_Largest(1, [1]), 1)

    def test_multiple_elements_same_frequency(self):
        self.assertEqual(frequency_Of_Largest(3, [1, 1, 2]), 1)

    def test_multiple_elements_different_frequency(self):
        self.assertEqual(frequency_Of_Largest(3, [1, 2, 1]), 2)

    def test_negative_numbers(self):
        self.assertEqual(frequency_Of_Largest(3, [-1, -2, -3]), 1)

    def test_duplicates_at_beginning(self):
        self.assertEqual(frequency_Of_Largest(2, [2, 2, 3]), 1)

    def test_duplicates_at_end(self):
        self.assertEqual(frequency_Of_Largest(2, [3, 2, 2]), 1)

    def test_duplicates_in_middle(self):
        self.assertEqual(frequency_Of_Largest(3, [3, 2, 2, 3]), 2)
