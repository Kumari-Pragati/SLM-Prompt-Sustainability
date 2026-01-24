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

    def test_all_same_elements(self):
        self.assertEqual(frequency([2, 2, 2, 2], 2), 4)

    def test_no_match(self):
        self.assertEqual(frequency([1, 2, 3, 4], 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(frequency([-1, -2, -2, -3], -2), 2)

    def test_mixed_types(self):
        self.assertEqual(frequency([1, '2', 3.0, '2'], '2'), 2)
