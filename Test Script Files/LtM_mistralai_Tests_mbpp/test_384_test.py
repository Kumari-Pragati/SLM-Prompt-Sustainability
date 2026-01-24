import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(frequency_Of_Smallest(3, [1, 1, 2]), 2)
        self.assertEqual(frequency_Of_Smallest(3, [1, 2, 3]), 1)
        self.assertEqual(frequency_Of_Smallest(3, [3, 3, 3]), 1)

    def test_edge_cases(self):
        self.assertEqual(frequency_Of_Smallest(0, []), 0)
        self.assertEqual(frequency_Of_Smallest(1, []), 0)
        self.assertEqual(frequency_Of_Smallest(1, [0]), 1)
        self.assertEqual(frequency_Of_Smallest(1, [-1]), 1)
        self.assertEqual(frequency_Of_Smallest(1, [2147483647]), 1)

    def test_complex(self):
        self.assertEqual(frequency_Of_Smallest(4, [1, 1, 2, 2]), 2)
        self.assertEqual(frequency_Of_Smallest(4, [1, 2, 1, 2]), 2)
        self.assertEqual(frequency_Of_Smallest(4, [1, 2, 2, 1]), 2)
        self.assertEqual(frequency_Of_Smallest(4, [2, 2, 1, 1]), 2)
        self.assertEqual(frequency_Of_Smallest(4, [-1, -1, 0, 0]), 2)
        self.assertEqual(frequency_Of_Smallest(4, [0, 0, -1, -1]), 2)
