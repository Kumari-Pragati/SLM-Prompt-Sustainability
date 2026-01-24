import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(frequency_Of_Smallest(4, [1, 1, 2, 3]), 4)
        self.assertEqual(frequency_Of_Smallest(5, [2, 2, 3, 3, 3]), 3)
        self.assertEqual(frequency_Of_Smallest(3, [-1, -1, 0]), 2)

    def test_edge_cases(self):
        self.assertEqual(frequency_Of_Smallest(0, []), 0)
        self.assertEqual(frequency_Of_Smallest(1, [0]), 1)
        self.assertEqual(frequency_Of_Smallest(2, [float('inf'), float('inf')]), 0)
        self.assertEqual(frequency_Of_Smallest(3, [-float('inf'), -float('inf'), -1]), 2)

    def test_boundary_cases(self):
        self.assertEqual(frequency_Of_Smallest(1, [0, 0]), 1)
        self.assertEqual(frequency_Of_Smallest(2, [1, 1]), 2)
        self.assertEqual(frequency_Of_Smallest(3, [2, 2, 2]), 3)
