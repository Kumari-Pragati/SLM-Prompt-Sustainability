import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_num([1, 2, 3]), 2.0)
        self.assertEqual(sum_num([0, 0, 0]), 0.0)
        self.assertEqual(sum_num([-1, -2, -3]), -1.0)

    def test_edge_case(self):
        self.assertEqual(sum_num([0]), 0.0)
        self.assertEqual(sum_num([1]), 1.0)
        self.assertEqual(sum_num([1, 2, 3, 4, 5]), 3.0)

    def test_corner_case(self):
        self.assertRaises(TypeError, sum_num, [1, 'a', 3])
        self.assertRaises(TypeError, sum_num, ['1', '2', '3'])
        self.assertRaises(TypeError, sum_num, [1, 2, 3, None])
