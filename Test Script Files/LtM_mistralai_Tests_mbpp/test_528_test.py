import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(min_length([1, 2, 3]), (1, 1))
        self.assertEqual(min_length([4, 4, 4]), (1, 4))
        self.assertEqual(min_length([5, 5, 5, 5]), (1, 5))

    def test_edge_cases(self):
        self.assertEqual(min_length([]), (0, None))
        self.assertEqual(min_length([None]), (1, None))
        self.assertEqual(min_length([0]), (0, 0))
        self.assertEqual(min_length([float('inf'), float('inf'), float('inf')]), (1, float('inf')))
        self.assertEqual(min_length([-float('inf'), -float('inf'), -float('inf')]), (1, -float('inf')))

    def test_complex_cases(self):
        self.assertEqual(min_length([1, 2, 3, 4, 5]), (1, 1))
        self.assertEqual(min_length([1, 2, 3, 4, 5, 5]), (1, 1))
        self.assertEqual(min_length([1, 2, 3, 4, 5, 5, 5]), (1, 1))
        self.assertEqual(min_length([1, 2, 3, 4, 5, 5, 5, 5]), (1, 1))
        self.assertEqual(min_length([1, 2, 3, 4, 5, 5, 5, 5, 5]), (1, 1))
        self.assertEqual(min_length([1, 2, 3, 4, 5, 5, 5, 5, 5, 5]), (1, 1))
        self.assertEqual(min_length([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5]), (1, 1))
        self.assertEqual(min_length([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5]), (1, 1))
