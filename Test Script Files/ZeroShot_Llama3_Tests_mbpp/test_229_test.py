import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):

    def test_re_arrange_array(self):
        self.assertEqual(re_arrange_array([-1, 2, 3, 4, 5], 3), [-1, 2, 3])
        self.assertEqual(re_arrange_array([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
        self.assertEqual(re_arrange_array([-1, -2, 3, 4, 5], 3), [-1, -2, 3])
        self.assertEqual(re_arrange_array([1, 2, 3, 4, 5], 2), [1, 2])
        self.assertEqual(re_arrange_array([-1, -2, -3, 4, 5], 3), [-1, -2, -3])
        self.assertEqual(re_arrange_array([1, 2, 3, 4, 5], 1), [1])
        self.assertEqual(re_arrange_array([-1, -2, -3, -4, -5], 5, [-5, -4, -3, -2, -1]), [-5, -4, -3, -2, -1])
        self.assertEqual(re_arrange_array([1, 2, 3, 4, 5], 0), [])
