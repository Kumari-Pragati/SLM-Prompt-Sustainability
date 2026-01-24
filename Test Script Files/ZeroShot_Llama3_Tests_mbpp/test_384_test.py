import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_frequency_Of_Smallest(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 2, 3, 3, 3]), 3)
        self.assertEqual(frequency_Of_Smallest(4, [1, 2, 3, 4]), 1)
        self.assertEqual(frequency_Of_Smallest(5, [1, 1, 1, 2, 2]), 2)
        self.assertEqual(frequency_Of_Smallest(3, [1, 1, 1]), 3)
        self.assertEqual(frequency_Of_Smallest(2, [1, 1]), 2)
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)
        self.assertEqual(frequency_Of_Smallest(4, [1, 2, 2, 2]), 2)
        self.assertEqual(frequency_Of_Smallest(5, [1, 1, 1, 2, 3]), 1)
        self.assertEqual(frequency_Of_Smallest(3, [1, 2, 2]), 2)
        self.assertEqual(frequency_Of_Smallest(4, [1, 1, 1, 1]), 1)
