import unittest
from mbpp_392_code import get_max_sum

class TestGetMaxSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_max_sum(1), 0)
        self.assertEqual(get_max_sum(2), 1)
        self.assertEqual(get_max_sum(3), 2)
        self.assertEqual(get_max_sum(4), 4)
        self.assertEqual(get_max_sum(5), 5)
        self.assertEqual(get_max_sum(6), 6)
        self.assertEqual(get_max_sum(7), 7)
        self.assertEqual(get_max_sum(8), 8)
        self.assertEqual(get_max_sum(9), 9)
        self.assertEqual(get_max_sum(10), 10)

    def test_edge_cases(self):
        self.assertEqual(get_max_sum(0), 0)
        self.assertEqual(get_max_sum(-1), 0)
        self.assertEqual(get_max_sum(11), 11)
        self.assertEqual(get_max_sum(100), 100)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_max_sum('a')
        with self.assertRaises(TypeError):
            get_max_sum(None)
        with self.assertRaises(TypeError):
            get_max_sum([])
        with self.assertRaises(TypeError):
            get_max_sum({})
