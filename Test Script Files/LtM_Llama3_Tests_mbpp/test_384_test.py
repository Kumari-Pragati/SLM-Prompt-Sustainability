import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(frequency_Of_Smallest(2, [1, 1]), 2)
        self.assertEqual(frequency_Of_Smallest(3, [1, 2, 1]), 2)
        self.assertEqual(frequency_Of_Smallest(4, [1, 2, 3, 1]), 2)

    def test_edge(self):
        self.assertEqual(frequency_Of_Smallest(0, []), 0)
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)
        self.assertEqual(frequency_Of_Smallest(2, [1, 1]), 2)
        self.assertEqual(frequency_Of_Smallest(2, [2, 2]), 1)
        self.assertEqual(frequency_Of_Smallest(2, [1, 2]), 1)

    def test_complex(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 4, 1]), 2)
        self.assertEqual(frequency_Of_Smallest(6, [1, 2, 3, 4, 5, 1]), 2)
        self.assertEqual(frequency_Of_Smallest(7, [1, 2, 3, 4, 5, 6, 1]), 2)
