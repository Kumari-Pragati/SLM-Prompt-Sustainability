import unittest
from mbpp_730_code import consecutive_duplicates

class TestConsecutiveDuplicates(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(consecutive_duplicates([1, 1, 2, 2, 3, 3]), [1, 2, 3])
        self.assertEqual(consecutive_duplicates(['a', 'a', 'b', 'b', 'c', 'c']), ['a', 'b', 'c'])

    def test_edge_conditions(self):
        self.assertEqual(consecutive_duplicates([]), [])
        self.assertEqual(consecutive_duplicates([1]), [1])
        self.assertEqual(consecutive_duplicates([1, 1]), [1])

    def test_complex_cases(self):
        self.assertEqual(consecutive_duplicates([1, 2, 2, 3, 3, 3]), [1, 2, 3])
        self.assertEqual(consecutive_duplicates(['a', 'b', 'b', 'c', 'c', 'c']), ['a', 'b', 'c'])
