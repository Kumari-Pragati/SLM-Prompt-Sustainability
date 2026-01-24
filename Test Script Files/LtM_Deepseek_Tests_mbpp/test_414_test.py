import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(overlapping([1, 2, 3], [3, 4, 5]), 1)
        self.assertEqual(overlapping([1, 2, 3], [4, 5, 6]), 0)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(overlapping([], []), 0)
        self.assertEqual(overlapping([1], []), 0)
        self.assertEqual(overlapping([], [1]), 0)
        self.assertEqual(overlapping([1], [1]), 1)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(overlapping([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), 1)
        self.assertEqual(overlapping([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), 0)
        self.assertEqual(overlapping([1, 2, 2, 3, 4], [2, 3, 4, 5, 6]), 1)
