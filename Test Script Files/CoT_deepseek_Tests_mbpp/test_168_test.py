import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency([1, 2, 3, 2, 4], 2), 2)

    def test_single_element_list(self):
        self.assertEqual(frequency([5], 5), 1)
        self.assertEqual(frequency([5], 6), 0)

    def test_empty_list(self):
        self.assertEqual(frequency([], 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(frequency([-1, -2, -2, -3], -2), 2)

    def test_mixed_types(self):
        self.assertEqual(frequency([1, '2', 3, '2', 4], '2'), 2)

    def test_non_integer_list(self):
        with self.assertRaises(TypeError):
            frequency(['1', '2', '3', '2', '4'], 2)

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            frequency(123, 2)
