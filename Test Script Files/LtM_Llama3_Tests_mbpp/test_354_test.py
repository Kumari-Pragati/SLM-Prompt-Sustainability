import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(tn_ap(1, 2, 1), 3)
        self.assertEqual(tn_ap(2, 3, 1), 5)
        self.assertEqual(tn_ap(3, 4, 1), 7)

    def test_edge(self):
        self.assertEqual(tn_ap(1, 1, 1), 1)
        self.assertEqual(tn_ap(1, 0, 1), 1)
        self.assertEqual(tn_ap(1, 1, 0), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            tn_ap('a', 2, 1)
        with self.assertRaises(TypeError):
            tn_ap(1, 'b', 1)
        with self.assertRaises(TypeError):
            tn_ap(1, 2, 'c')
