import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(frequency_Of_Largest(3, [1, 2, 3]), 1)
        self.assertEqual(frequency_Of_Largest(3, [3, 3, 3]), 1)
        self.assertEqual(frequency_Of_Largest(3, [2, 3, 3]), 1)

    def test_edge_and_boundary(self):
        self.assertEqual(frequency_Of_Largest(0, []), 0)
        self.assertEqual(frequency_Of_Largest(1, [0]), 1)
        self.assertEqual(frequency_Of_Largest(1, [-1]), 1)
        self.assertEqual(frequency_Of_Largest(1, [1000000000]), 1)

    def test_complex(self):
        self.assertEqual(frequency_Of_Largest(4, [1, 1, 2, 3]), 1)
        self.assertEqual(frequency_Of_Largest(4, [3, 3, 3, 3]), 1)
        self.assertEqual(frequency_Of_Largest(4, [2, 2, 3, 3]), 1)
        self.assertEqual(frequency_Of_Largest(4, [1, 2, 2, 3]), 1)
