import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(count_no(2, 3, 1, 5), 3)
        self.assertEqual(count_no(3, 4, 1, 9), 9)
        self.assertEqual(count_no(5, 1, 1, 5), 5)

    def test_edge_cases(self):
        self.assertEqual(count_no(2, 1, 1, 2), 2)
        self.assertEqual(count_no(2, 1, 2, 2), 2)
        self.assertEqual(count_no(2, 1, 1, 0), 0)
        self.assertEqual(count_no(2, 1, 10, 10), 10)

    def test_boundary_cases(self):
        self.assertEqual(count_no(2, 1, 0, 1), 0)
        self.assertEqual(count_no(2, 1, 1, 0), 0)
        self.assertEqual(count_no(2, 1, 1, 2147483647), 2147483647)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_no, 'a', 1, 1, 5)
        self.assertRaises(TypeError, count_no, 1, 'b', 1, 5)
        self.assertRaises(TypeError, count_no, 1, 1, 'a', 5)
        self.assertRaises(TypeError, count_no, 1, 1, 1, 'a')
        self.assertRaises(ValueError, count_no, 0, 1, 1, 1)
        self.assertRaises(ValueError, count_no, 1, 0, 1, 1)
        self.assertRaises(ValueError, count_no, 1, 1, 0, 1)
        self.assertRaises(ValueError, count_no, 1, 1, 1, 0)
