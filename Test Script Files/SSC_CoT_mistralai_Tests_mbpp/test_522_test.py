import unittest
from mbpp_522_code import lbs

class TestLbsFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(lbs([1, 5, 4, 3]), 5)
        self.assertEqual(lbs([3, 2, 6, 4]), 5)
        self.assertEqual(lbs([10, 22, 9, 33, 21]), 33)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(lbs([0]), 0)
        self.assertEqual(lbs([1]), 1)
        self.assertEqual(lbs([1, 1]), 1)
        self.assertEqual(lbs([1, 1, 1]), 1)
        self.assertEqual(lbs([1, 1, 1, 1]), 1)
        self.assertEqual(lbs([1000000000]), 1000000000)

    def test_negative_input(self):
        self.assertRaises(ValueError, lbs, [-1])
        self.assertRaises(ValueError, lbs, [-1, -2, -3])

    def test_zero_duplicates(self):
        self.assertEqual(lbs([0, 0]), 0)
        self.assertEqual(lbs([0, 0, 0]), 0)
        self.assertEqual(lbs([0, 0, 0, 0]), 0)

    def test_all_same_positive(self):
        self.assertEqual(lbs([1, 1, 1]), 1)
        self.assertEqual(lbs([5, 5, 5]), 5)
        self.assertEqual(lbs([10, 10, 10]), 10)

    def test_all_same_negative(self):
        self.assertEqual(lbs([-1, -1, -1]), 0)
        self.assertEqual(lbs([-5, -5, -5]), 0)
        self.assertEqual(lbs([-10, -10, -10]), 0)

    def test_empty_list(self):
        self.assertEqual(lbs([]), 0)
