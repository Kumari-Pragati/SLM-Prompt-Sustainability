import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(frequency_Of_Largest(0, []), 0)

    def test_single_element(self):
        for num in range(10):
            self.assertEqual(frequency_Of_Largest(1, [num]), 1)

    def test_multiple_elements_same_frequency(self):
        arr = [1, 1, 2, 2, 3, 3]
        self.assertEqual(frequency_Of_Largest(6, arr), 3)

    def test_multiple_elements_different_frequency(self):
        arr = [1, 2, 2, 3, 3, 4]
        self.assertEqual(frequency_Of_Largest(6, arr), 1)

    def test_negative_numbers(self):
        arr = [-1, -2, -2, -3]
        self.assertEqual(frequency_Of_Largest(4, arr), 1)

    def test_duplicate_first_element(self):
        self.assertEqual(frequency_Of_Largest(1, [1, 1]), 1)

    def test_duplicate_last_element(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 2, 2, 2]), 1)

    def test_duplicate_middle_element(self):
        self.assertEqual(frequency_Of_Largest(7, [1, 1, 2, 2, 2, 3, 3]), 2)

    def test_single_negative_number(self):
        self.assertEqual(frequency_Of_Largest(1, [-1]), 1)

    def test_single_positive_number(self):
        self.assertEqual(frequency_Of_Largest(1, [1]), 1)

    def test_single_zero(self):
        self.assertEqual(frequency_Of_Largest(1, [0]), 1)
