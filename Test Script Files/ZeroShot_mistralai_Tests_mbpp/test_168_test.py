import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(frequency([]), 0)

    def test_single_element(self):
        self.assertEqual(frequency([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(frequency([1, 1, 2, 1, 2, 3]), 3)

    def test_negative_number(self):
        self.assertEqual(frequency([-1, -1, 0, -1], -1), 2)

    def test_non_existent_number(self):
        self.assertEqual(frequency([1, 2, 3], 4), 0)
