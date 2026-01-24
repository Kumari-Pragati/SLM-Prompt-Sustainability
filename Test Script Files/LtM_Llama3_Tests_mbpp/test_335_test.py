import unittest
from mbpp_335_code import ap_sum

class TestApSum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(ap_sum(1, 1, 1), 1)
        self.assertEqual(ap_sum(2, 2, 1), 4)
        self.assertEqual(ap_sum(3, 3, 1), 9)

    def test_edge_cases(self):
        self.assertEqual(ap_sum(0, 1, 1), 0)
        self.assertEqual(ap_sum(1, 0, 1), 0)
        self.assertEqual(ap_sum(1, 1, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            ap_sum('a', 1, 1)
        with self.assertRaises(TypeError):
            ap_sum(1, 'a', 1)
        with self.assertRaises(TypeError):
            ap_sum(1, 1, 'a')
