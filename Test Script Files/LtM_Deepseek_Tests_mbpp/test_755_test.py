import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(second_smallest([2, 1, 3]), 2)
        self.assertEqual(second_smallest([1, 2, 2]), 2)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertIsNone(second_smallest([]))
        self.assertIsNone(second_smallest([1]))
        self.assertIsNone(second_smallest([1, 1]))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(second_smallest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 2)
        self.assertEqual(second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 2)
        self.assertEqual(second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]), 2)
        self.assertEqual(second_smallest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9]), 9)
