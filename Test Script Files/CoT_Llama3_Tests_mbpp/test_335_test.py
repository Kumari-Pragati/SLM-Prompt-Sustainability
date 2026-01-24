import unittest
from mbpp_335_code import ap_sum

class TestApSum(unittest.TestCase):
    def test_ap_sum_typical(self):
        self.assertEqual(ap_sum(1, 5, 2), 9)

    def test_ap_sum_edge(self):
        self.assertEqual(ap_sum(1, 1, 2), 1)
        self.assertEqual(ap_sum(1, 0, 2), 0)

    def test_ap_sum_invalid_input(self):
        with self.assertRaises(TypeError):
            ap_sum('a', 5, 2)
        with self.assertRaises(TypeError):
            ap_sum(1, 'a', 2)
        with self.assertRaises(TypeError):
            ap_sum(1, 5, 'a')

    def test_ap_sum_boundary(self):
        self.assertEqual(ap_sum(1, 1, 1), 1)
        self.assertEqual(ap_sum(1, 0, 1), 0)
