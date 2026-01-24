import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(12,15), 3)
        self.assertEqual(sum(4,6), 2)
        self.assertEqual(sum(10,20), 2)
        self.assertEqual(sum(1,1), 0)
        self.assertEqual(sum(2,3), 1)
        self.assertEqual(sum(5,5), 1)
        self.assertEqual(sum(7,7), 1)
        self.assertEqual(sum(8,8), 1)
        self.assertEqual(sum(9,9), 1)
        self.assertEqual(sum(10,10), 1)
        self.assertEqual(sum(11,11), 1)
        self.assertEqual(sum(12,12), 1)
        self.assertEqual(sum(13,13), 1)
        self.assertEqual(sum(14,14), 1)
        self.assertEqual(sum(15,15), 1)
        self.assertEqual(sum(16,16), 1)
        self.assertEqual(sum(17,17), 1)
        self.assertEqual(sum(18,18), 1)
        self.assertEqual(sum(19,19), 1)
        self.assertEqual(sum(20,20), 1)

    def test_sum_edge(self):
        self.assertEqual(sum(1,1), 0)
        self.assertEqual(sum(2,2), 1)
        self.assertEqual(sum(3,3), 1)
        self.assertEqual(sum(4,4), 2)
        self.assertEqual(sum(5,5), 1)
        self.assertEqual(sum(6,6), 2)
        self.assertEqual(sum(7,7), 1)
        self.assertEqual(sum(8,8), 2)
        self.assertEqual(sum(9,9), 1)
        self.assertEqual(sum(10,10), 2)

    def test_sum_invalid(self):
        with self.assertRaises(TypeError):
            sum('a', 10)
        with self.assertRaises(TypeError):
            sum(10, 'b')
