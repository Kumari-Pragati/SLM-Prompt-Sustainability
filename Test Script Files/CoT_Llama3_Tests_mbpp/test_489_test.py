import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 3, 4]), 1)

    def test_edge_case(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 5, 5, 5, 5]), 5)

    def test_edge_case2(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 4, 5]), 1)

    def test_edge_case3(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 4, 3, 2, 1]), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            frequency_Of_Largest('a', [1, 2, 3, 4, 5])

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            frequency_Of_Largest(5, 'a')
