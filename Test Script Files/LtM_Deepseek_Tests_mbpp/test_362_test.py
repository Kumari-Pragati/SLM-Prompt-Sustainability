import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3]), 3)
        self.assertEqual(max_occurrences([4, 4, 4, 4]), 4)

    def test_edge_conditions(self):
        self.assertEqual(max_occurrences([1]), 1)
        self.assertEqual(max_occurrences([]), None)

    def test_complex_cases(self):
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), 4)
        self.assertEqual(max_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]), 4)
        self.assertEqual(max_occurrences([1, 1, 1, 2, 2, 2, 3, 3, 3]), 1)
