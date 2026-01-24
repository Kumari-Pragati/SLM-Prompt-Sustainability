import unittest
from mbpp_522_code import lbs

class TestLBS(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(lbs([1, 2, 3, 4, 5]), 5)
        self.assertEqual(lbs([5, 4, 3, 2, 1]), 5)
        self.assertEqual(lbs([1, 3, 5, 7, 9]), 5)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(lbs([]), 0)
        self.assertEqual(lbs([1]), 1)
        self.assertEqual(lbs([1, 1]), 2)
        self.assertEqual(lbs([1, 2, 1]), 3)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(lbs([10, 22, 9, 33, 21, 50, 41, 60, 80]), 5)
        self.assertEqual(lbs([10, 22, 9, 33, 21, 50, 41, 60, 80, 100]), 6)
        self.assertEqual(lbs([1, 2, 3, 4, 5, 4, 3, 2, 1]), 5)
