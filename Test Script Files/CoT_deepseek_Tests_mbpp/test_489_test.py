import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 3, 2]), 1)

    def test_largest_is_first(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 2, 3, 3, 2]), 1)

    def test_largest_is_last(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 3, 5]), 1)

    def test_largest_in_middle(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 5, 3, 2]), 2)

    def test_all_same(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 1, 1, 1]), 5)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            frequency_Of_Largest(0, [])

    def test_negative_numbers(self):
        self.assertEqual(frequency_Of_Largest(5, [-1, -2, -3, -3, -2]), 1)

    def test_large_numbers(self):
        self.assertEqual(frequency_Of_Largest(5, [1000, 2000, 3000, 3000, 2000]), 2)
