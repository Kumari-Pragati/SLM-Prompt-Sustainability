import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(frequency_Of_Smallest(0, []), 0)

    def test_single_element(self):
        for num in range(10):
            self.assertEqual(frequency_Of_Smallest(1, [num]), 1)

    def test_multiple_elements(self):
        arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.assertEqual(frequency_Of_Smallest(10, arr), 2)

    def test_minimum_element_not_found(self):
        self.assertEqual(frequency_Of_Smallest(1, [2, 3, 4]), 0)

    def test_minimum_element_found_once(self):
        self.assertEqual(frequency_Of_Smallest(1, [1, 2, 3]), 1)

    def test_minimum_element_found_multiple_times(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 1, 2, 2, 3]), 2)

    def test_negative_numbers(self):
        arr = [-1, -1, 0, 0, 1]
        self.assertEqual(frequency_Of_Smallest(5, arr), 2)
