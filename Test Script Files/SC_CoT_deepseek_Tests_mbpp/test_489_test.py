import unittest

from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 3, 2]), 1)

    def test_edge_case_single_largest(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 1, 1, 1]), 5)

    def test_edge_case_all_same(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 5, 5, 5, 5]), 5)

    def test_edge_case_empty_array(self):
        self.assertEqual(frequency_Of_Largest(0, []), None)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(frequency_Of_Largest(5, [-1, -2, -3, -2, -1]), 2)

    def test_invalid_input_negative_size(self):
        with self.assertRaises(IndexError):
            frequency_Of_Largest(-5, [1, 2, 3, 4, 5])

    def test_invalid_input_size_greater_than_array(self):
        with self.assertRaises(IndexError):
            frequency_Of_Largest(6, [1, 2, 3, 4, 5])
