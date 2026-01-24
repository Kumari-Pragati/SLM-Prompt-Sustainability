import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(frequency_Of_Smallest(0, []), 0)

    def test_single_element(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)

    def test_multiple_elements_same_value(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 1, 1]), 3)

    def test_multiple_elements_different_values(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 2, 3]), 1)

    def test_minimum_value_at_beginning(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 2, 1]), 2)

    def test_minimum_value_at_end(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 2, 1]), 2)

    def test_minimum_value_in_middle(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 2, 1]), 2)

    def test_negative_numbers(self):
        self.assertEqual(frequency_Of_Smallest(3, [-1, -2, -3]), 1)

    def test_floats(self):
        self.assertEqual(frequency_Of_Smallest(3, [1.1, 2.2, 3.3]), 1)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            frequency_Of_Smallest(-1, [])

    def test_invalid_input_negative_n(self):
        with self.assertRaises(ValueError):
            frequency_Of_Smallest(-1, [1])
