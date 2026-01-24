import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(second_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(second_smallest([5, 3, 2, 1]), 3)
        self.assertEqual(second_smallest([-1, 0, 1, 2]), 0)

    def test_edge_cases(self):
        self.assertEqual(second_smallest([1]), None)
        self.assertEqual(second_smallest([1, 1]), 1)
        self.assertEqual(second_smallest([1, 2, 1]), 1)
        self.assertEqual(second_smallest([1, 2, 3, 1]), 1)
        self.assertEqual(second_smallest([1, 2, 3, 4, 1]), 2)
        self.assertEqual(second_smallest([1, 2, 3, 4, 5, 1]), 3)

    def test_invalid_inputs(self):
        self.assertIsNone(second_smallest([]))
        self.assertIsNone(second_smallest([None]))
        self.assertIsNone(second_smallest([1, 'a']))
        self.assertIsNone(second_smallest([1, 2, 3, 'a']))
