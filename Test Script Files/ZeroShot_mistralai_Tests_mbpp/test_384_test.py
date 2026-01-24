import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(frequency_Of_Smallest(0, []), 0)

    def test_single_element(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 1, 2]), 2)

    def test_duplicates(self):
        self.assertEqual(frequency_Of_Smallest(4, [1, 1, 1, 2]), 3)

    def test_negative_numbers(self):
        self.assertEqual(frequency_Of_Smallest(3, [-1, -1, 0]), 2)

    def test_zero(self):
        self.assertEqual(frequency_Of_Smallest(1, [0]), 1)

    def test_larger_numbers(self):
        self.assertEqual(frequency_Of_Smallest(3, [2, 1, 1]), 2)
