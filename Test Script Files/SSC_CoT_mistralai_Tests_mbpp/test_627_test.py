import unittest
from mbpp_627_code import range
from six.moves import xrange

class TestFindFirstMissing(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_First_Missing([2, 3, 4, 6, 7, 8, 9], 0, 8), 5)
        self.assertEqual(find_First_Missing([-1, 0, 1, 2, 3, 4, 5], 0, 5), -1)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5], 0, 5), 6)

    def test_edge_cases(self):
        self.assertEqual(find_First_Missing([], 0, 0), 1)
        self.assertEqual(find_First_Missing([1], 0, 0), 1)
        self.assertEqual(find_First_Missing([1, 1], 0, 1), 2)
        self.assertEqual(find_First_Missing([1, 2, 2], 0, 2), 3)
        self.assertEqual(find_First_Missing([1, 2, 3], 0, 2), 4)
        self.assertEqual(find_First_Missing([1, 2, 3, 4], 0, 3), 5)
        self.assertEqual(find_First_Missing([1, 2, 3, 4, 5], 0, 4), 6)
        self.assertEqual(find_First_Missing([1, 2, 3, 4, 5, 6], 0, 5), 7)

    def test_boundary_cases(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4], 0, 4), 5)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4], 4, 4), 5)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4], 5, 4), 5)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4], -1, 4), 0)
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4], 0, -1), 0)

    def test_invalid_inputs(self):
        self.assertRaises(IndexError, find_First_Missing, [1, 2, 3], 4, -1)
        self.assertRaises(IndexError, find_First_Missing, [1, 2, 3], -1, 4)
        self.assertRaises(IndexError, find_First_Missing, [], 0, 0)
        self.assertRaises(TypeError, find_First_Missing, [1, 2, 3], 'a', 0)
