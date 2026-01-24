import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):
    def test_single_element_array(self):
        self.assertEqual(frequency_Of_Largest(1, [5]), 1)

    def test_multiple_elements_array(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 5, 5, 5, 5]), 5)

    def test_array_with_multiple_largest_elements(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 5, 5, 3, 5]), 4)

    def test_array_with_no_largest_elements(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 4, 5]), 1)

    def test_array_with_negative_numbers(self):
        self.assertEqual(frequency_Of_Largest(5, [-5, -5, -5, -5, -5]), 5)

    def test_array_with_zero(self):
        self.assertEqual(frequency_Of_Largest(5, [0, 0, 0, 0, 0]), 5)
