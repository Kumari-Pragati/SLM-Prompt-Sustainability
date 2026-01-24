import unittest
from489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(frequency_Of_Largest(0, []), 0)

    def test_single_element(self):
        for num in range(10):
            self.assertEqual(frequency_Of_Largest(1, [num]), 1)

    def test_multiple_elements(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        self.assertEqual(frequency_Of_Largest(len(arr), arr), 1)

    def test_duplicates(self):
        arr = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        self.assertEqual(frequency_Of_Largest(len(arr), arr), 4)

    def test_negative_numbers(self):
        arr = [-1, -2, -2, -3, -3, -3, -4, -4, -4, -4]
        self.assertEqual(frequency_Of_Largest(len(arr), arr), 1)

    def test_zero(self):
        self.assertEqual(frequency_Of_Largest(0, []), 0)
        self.assertEqual(frequency_Of_Largest(0, [0]), 1)
        self.assertEqual(frequency_Of_Largest(0, [-0]), 1)

    def test_large_numbers(self):
        arr = [1000000001, 1000000002, 1000000002, 1000000003, 1000000003, 1000000003, 1000000004, 1000000004, 1000000004, 1000000004]
        self.assertEqual(frequency_Of_Largest(len(arr), arr), 1)
