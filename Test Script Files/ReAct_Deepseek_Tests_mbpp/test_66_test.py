import unittest
from mbpp_66_code import pos_count

class TestPosCount(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(pos_count([1, -2, 3, -4, 5]), 4)
        self.assertEqual(pos_count([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(pos_count([0, 0, 0, 0, 0]), 1)

    def test_edge_cases(self):
        self.assertEqual(pos_count([]), 0)
        self.assertEqual(pos_count([1]), 1)
        self.assertEqual(pos_count([-1]), 0)
        self.assertEqual(pos_count([0]), 1)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            pos_count(123)
        with self.assertRaises(TypeError):
            pos_count('123')
        with self.assertRaises(TypeError):
            pos_count(None)
