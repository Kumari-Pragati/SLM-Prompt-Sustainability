import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)
        self.assertEqual(test_three_equal(3, 4, 5), 0)
        self.assertEqual(test_three_equal('a', 'b', 'c'), 0)

    def test_edge_cases(self):
        self.assertEqual(test_three_equal(1, 1, 1), 0)
        self.assertEqual(test_three_equal('a', 'a', 'a'), 0)
        self.assertEqual(test_three_equal(1, 2, 2), 1)
        self.assertEqual(test_three_equal('a', 'b', 'a'), 1)

    def test_boundary_cases(self):
        self.assertEqual(test_three_equal(1, 2, 4), 1)
        self.assertEqual(test_three_equal('a', 'b', 'z'), 1)
        self.assertEqual(test_three_equal(1, 2.5, 3), 1)
        self.assertEqual(test_three_equal('a', 'b', 'z'), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, test_three_equal, 1, 'a', 'b')
        self.assertRaises(TypeError, test_three_equal, 'a', 1, 'b')
        self.assertRaises(TypeError, test_three_equal, 'a', 'b', 1)
        self.assertRaises(TypeError, test_three_equal, (1, 2, 'a'))
        self.assertRaises(TypeError, test_three_equal, ['1', '2', '3'])
