import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):
    def test_single_element_array(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)

    def test_multiple_elements_same_value(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 1, 1]), 3)

    def test_multiple_elements_different_values(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 2, 3]), 1)

    def test_empty_array(self):
        self.assertEqual(frequency_Of_Smallest(0, []), 0)

    def test_array_with_zero(self):
        self.assertEqual(frequency_Of_Smallest(3, [0, 1, 2]), 0)

    def test_array_with_negative_numbers(self):
        self.assertEqual(frequency_Of_Smallest(3, [-1, 0, 1]), 1)
