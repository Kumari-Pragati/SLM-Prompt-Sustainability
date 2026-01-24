import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(frequency_Of_Largest(2, [1, 1]), 1)
        self.assertEqual(frequency_Of_Largest(2, [2, 2]), 1)
        self.assertEqual(frequency_Of_Largest(2, [1, 2]), 1)
        self.assertEqual(frequency_Of_Largest(3, [1, 1, 1]), 3)
        self.assertEqual(frequency_Of_Largest(3, [1, 2, 2]), 2)

    def test_edge(self):
        self.assertEqual(frequency_Of_Largest(0, []), 0)
        self.assertEqual(frequency_Of_Largest(1, [1]), 1)
        self.assertEqual(frequency_Of_Largest(1, [2]), 1)
        self.assertEqual(frequency_Of_Largest(2, [1, 1]), 1)
        self.assertEqual(frequency_Of_Largest(2, [1, 2]), 1)

    def test_complex(self):
        self.assertEqual(frequency_Of_Largest(3, [1, 2, 3]), 1)
        self.assertEqual(frequency_Of_Largest(4, [1, 1, 2, 2]), 2)
        self.assertEqual(frequency_Of_Largest(4, [1, 2, 2, 3]), 1)
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 1, 2, 2]), 3)
