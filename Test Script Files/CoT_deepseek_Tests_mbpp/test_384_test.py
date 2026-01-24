import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 2, 1]), 2)

    def test_single_element(self):
        self.assertEqual(frequency_Of_Smallest(1, [5]), 1)

    def test_all_same_elements(self):
        self.assertEqual(frequency_Of_Smallest(5, [3, 3, 3, 3, 3]), 5)

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            frequency_Of_Smallest(0, [])

    def test_negative_numbers(self):
        self.assertEqual(frequency_Of_Smallest(5, [-1, -2, -3, -2, -1]), 2)

    def test_mixed_numbers(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, -2, 3, -2, 1]), 2)
