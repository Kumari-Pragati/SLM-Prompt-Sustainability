import unittest
from489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Largest(3, [1, 2, 3]), 1)
        self.assertEqual(frequency_Of_Largest(3, [3, 3, 3]), 1)
        self.assertEqual(frequency_Of_Largest(4, [4, 4, 4, 4]), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(frequency_Of_Largest(1, [1]), 1)

    def test_edge_case_no_largest(self):
        self.assertEqual(frequency_Of_Largest(3, [1, 2, 0]), 0)

    def test_edge_case_multiple_maxima(self):
        self.assertEqual(frequency_Of_Largest(4, [3, 3, 2, 3]), 2)

    def test_corner_case_empty_list(self):
        self.assertEqual(frequency_Of_Largest(0, []), 0)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(frequency_Of_Largest(4, [-1, -2, -3, 0]), 1)
