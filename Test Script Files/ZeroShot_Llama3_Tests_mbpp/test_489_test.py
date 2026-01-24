import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_frequency_of_largest(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 4, 5]), 1)
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 2, 2, 3]), 1)
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 2, 3, 3]), 2)
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 1, 2, 2]), 3)
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 1, 1, 1]), 5)
        self.assertEqual(frequency_Of_Largest(5, [5, 5, 5, 5, 5]), 5)
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 4, 5]), 1)
        self.assertEqual(frequency_Of_Largest(5, [5, 4, 3, 2, 1]), 1)
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 2, 2, 3]), 1)
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 4, 5, 5]), 1)

    def test_frequency_of_largest_edge_cases(self):
        self.assertEqual(frequency_Of_Largest(1, [1]), 1)
        self.assertEqual(frequency_Of_Largest(1, [1, 1]), 1)
        self.assertEqual(frequency_Of_Largest(1, [1, 1, 1]), 1)
        self.assertEqual(frequency_Of_Largest(1, [1, 1, 1, 1]), 1)
        self.assertEqual(frequency_Of_Largest(1, [1, 1, 1, 1, 1]), 1)
