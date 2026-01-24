import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(frequency_Of_Largest(1, [5]), 1)

    def test_all_same_elements(self):
        self.assertEqual(frequency_Of_Largest(5, [3, 3, 3, 3, 3]), 5)

    def test_mixed_elements(self):
        self.assertEqual(frequency_Of_Largest(6, [1, 2, 3, 4, 5, 5]), 2)

    def test_empty_array(self):
        self.assertEqual(frequency_Of_Largest(0, []), None)

    def test_negative_elements(self):
        self.assertEqual(frequency_Of_Largest(5, [-1, -2, -3, -4, -5]), 1)

    def test_large_array(self):
        self.assertEqual(frequency_Of_Largest(100000, [i for i in range(100000)]), 1)
