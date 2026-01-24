import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(get_equal([(1, 2, 3), (1, 2, 3), (1, 2, 3)], 3), ("All tuples have same length"))
        self.assertEqual(get_equal([(1, 2), (1, 2), (1, 2)], 2), ("All tuples have same length"))

    def test_edge_cases(self):
        self.assertEqual(get_equal([(1, 2, 3), (1, 2), (1, 2, 3)], 3), ("All tuples have same length"))
        self.assertEqual(get_equal([(1, 2), (1, 2, 3), (1, 2)], 3), ("All tuples do not have same length"))
        self.assertEqual(get_equal([(1, 2), (1, 2)], 2), ("All tuples have same length"))
        self.assertEqual(get_equal([(1, 2), (1, 2, 3)], 3), ("All tuples do not have same length"))
        self.assertEqual(get_equal([(1, 2), (1, 2, 3)], 2), ("All tuples do not have same length"))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_equal, [1, 2, 3], 2)
        self.assertRaises(TypeError, get_equal, [(1, 2), '3'], 2)
        self.assertRaises(TypeError, get_equal, [(1, 2), (1, 2), '3'], 2)
