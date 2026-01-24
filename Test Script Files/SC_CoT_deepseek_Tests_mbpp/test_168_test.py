import unittest

from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency([1, 2, 3, 2, 4], 2), 2)

    def test_empty_list(self):
        self.assertEqual(frequency([], 2), 0)

    def test_single_element_list(self):
        self.assertEqual(frequency([2], 2), 1)
        self.assertEqual(frequency([2], 3), 0)

    def test_no_matching_elements(self):
        self.assertEqual(frequency([1, 2, 3, 4], 5), 0)

    def test_large_list(self):
        self.assertEqual(frequency([i for i in range(1000000)], 500000), 1)

    def test_negative_numbers(self):
        self.assertEqual(frequency([-1, -2, -3, -2, -4], -2), 1)

    def test_float_numbers(self):
        self.assertEqual(frequency([1.1, 2.2, 3.3, 2.2, 4.4], 2.2), 1)

    def test_string_elements(self):
        self.assertEqual(frequency(['a', 'b', 'c', 'b', 'd'], 'b'), 1)

    def test_mixed_type_elements(self):
        with self.assertRaises(TypeError):
            frequency([1, 'a', 2.0, 'b', 3], 1)
