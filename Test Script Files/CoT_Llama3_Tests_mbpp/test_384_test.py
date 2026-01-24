import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 3, 1]), 2)

    def test_edge_case(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)

    def test_edge_case2(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 1, 1, 1, 1]), 5)

    def test_edge_case3(self):
        self.assertEqual(frequency_Of_Smallest(5, [5, 5, 5, 5, 5]), 1)

    def test_edge_case4(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 4, 5]), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            frequency_Of_Smallest('a', [1, 2, 3, 4, 5])

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            frequency_Of_Smallest(5, 'a')
