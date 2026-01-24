import unittest
from mbpp_442_code import positive_count

class TestPositiveCount(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(positive_count([1, 2, 3, 4]), 1.0)
        self.assertAlmostEqual(positive_count([0, 1, 2, 3, 4]), 0.4)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(positive_count([0]), 1.0)
        self.assertAlmostEqual(positive_count([1]), 1.0)
        self.assertAlmostEqual(positive_count([-1]), 0.0)
        self.assertAlmostEqual(positive_count([-1, 0]), 0.0)
        self.assertAlmostEqual(positive_count([-1, 0, 1]), 0.33)
        self.assertAlmostEqual(positive_count([-1, 0, 1, 2]), 0.5)
        self.assertAlmostEqual(positive_count([-1, 0, 1, 2, 3]), 0.6)
        self.assertAlmostEqual(positive_count([-1, 0, 1, 2, 3, 4]), 0.8)

    def test_invalid_input(self):
        # If the function doesn't explicitly handle invalid inputs,
        # you can skip this test method.
        self.assertRaises(TypeError, positive_count, [1, "two", 3])
        self.assertRaises(TypeError, positive_count, ["one", 2, 3])
