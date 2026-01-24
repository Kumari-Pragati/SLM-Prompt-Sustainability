import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rearrange_numbs([3, 1, 2]), [1, 2, 3])
        self.assertEqual(rearrange_numbs([0, 1, 2]), [0, 1, 2])
        self.assertEqual(rearrange_numbs([-1, -2, -3]), [-1, -2, -3])

    def test_edge_cases(self):
        self.assertEqual(rearrange_numbs([0, 0, 0]), [0, 0, 0])
        self.assertEqual(rearrange_numbs([1]), [1])
        self.assertEqual(rearrange_numbs([]), [])

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            rearrange_numbs(None)
        with self.assertRaises(TypeError):
            rearrange_numbs('123')
        with self.assertRaises(TypeError):
            rearrange_numbs([1, 'a', 2])
