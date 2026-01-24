import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(frequency_Of_Largest(3, [1, 2, 3]), 1)
        self.assertEqual(frequency_Of_Largest(3, [3, 3, 3]), 1)
        self.assertEqual(frequency_Of_Largest(4, [4, 4, 4, 4]), 1)

    def test_edge_cases(self):
        self.assertEqual(frequency_Of_Largest(0, []), 0)
        self.assertEqual(frequency_Of_Largest(1, [0]), 1)
        self.assertEqual(frequency_Of_Largest(2, [0, 0]), 1)
        self.assertEqual(frequency_Of_Largest(3, [1, 0, 1]), 1)
        self.assertEqual(frequency_Of_Largest(4, [1, 0, 1, 1]), 1)

    def test_boundary_cases(self):
        self.assertEqual(frequency_Of_Largest(1, [1, -1]), 1)
        self.assertEqual(frequency_Of_Largest(2, [-1, -1]), 1)
        self.assertEqual(frequency_Of_Largest(3, [-1, 0, -1]), 1)
        self.assertEqual(frequency_Of_Largest(4, [-1, 0, 1, -1]), 1)
