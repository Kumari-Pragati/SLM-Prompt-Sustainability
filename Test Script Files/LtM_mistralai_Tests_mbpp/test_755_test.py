import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(second_smallest([1, 2]), 1)
        self.assertEqual(second_smallest([2, 3]), 2)
        self.assertEqual(second_smallest([3, 2]), 2)
        self.assertEqual(second_smallest([4, 5, 6]), 4)

    def test_edge_cases(self):
        self.assertEqual(second_smallest([1]), None)
        self.assertEqual(second_smallest([2]), None)
        self.assertEqual(second_smallest([2, 2]), 2)
        self.assertEqual(second_smallest([1, 1]), None)
        self.assertEqual(second_smallest([1, 1, 1]), None)
        self.assertEqual(second_smallest([-10, -20, -30]), -10)
        self.assertEqual(second_smallest([30, 20, 10]), 20)

    def test_complex_cases(self):
        self.assertEqual(second_smallest([1, 2, 1]), 1)
        self.assertEqual(second_smallest([2, 1, 2]), 1)
        self.assertEqual(second_smallest([1, 2, 3, 1]), 1)
        self.assertEqual(second_smallest([3, 2, 1, 2]), 2)
        self.assertEqual(second_smallest([1, 2, 3, 4, 1]), 2)
        self.assertEqual(second_smallest([4, 3, 2, 1]), 2)
        self.assertEqual(second_smallest([1, 2, 3, 4, 5]), 2)
