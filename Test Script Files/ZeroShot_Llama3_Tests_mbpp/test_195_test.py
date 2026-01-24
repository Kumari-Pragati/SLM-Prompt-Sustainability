import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):

    def test_first_function(self):
        self.assertEqual(first([1,2,3,4,5], 3, 5), 2)
        self.assertEqual(first([1,2,3,4,5], 0, 5), 0)
        self.assertEqual(first([1,2,3,4,5], 5, 5), 4)
        self.assertEqual(first([1,2,3,4,5], 6, 5), -1)
        self.assertEqual(first([1,2,3,4,5], 1, 5), 0)
        self.assertEqual(first([1,2,3,4,5], 5, 5), 4)
        self.assertEqual(first([1,2,3,4,5], 4, 5), 3)
        self.assertEqual(first([1,2,3,4,5], 3, 5), 2)
        self.assertEqual(first([1,2,3,4,5], 2, 5), 1)

    def test_first_function_edge_cases(self):
        self.assertEqual(first([], 1, 0), -1)
        self.assertEqual(first([1], 1, 1), 0)
        self.assertEqual(first([1], 2, 1), -1)
        self.assertEqual(first([1,2], 1, 2), 0)
        self.assertEqual(first([1,2], 2, 2), 1)
