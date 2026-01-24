import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_frequency(self):
        self.assertEqual(frequency([1, 2, 3, 4, 5], 3), 1)
        self.assertEqual(frequency([1, 2, 2, 3, 4], 2), 2)
        self.assertEqual(frequency([1, 1, 1, 2, 3], 1), 3)
        self.assertEqual(frequency([1, 2, 3, 4, 5], 6), 0)
        self.assertEqual(frequency([], 5), 0)
        self.assertEqual(frequency([1, 2, 3, 4, 5], 1), 1)
