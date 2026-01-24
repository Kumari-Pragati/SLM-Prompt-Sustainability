import unittest
from mbpp_66_code import pos_count

class TestPosCount(unittest.TestCase):

    def test_pos_count(self):
        self.assertEqual(pos_count([1, 2, 3, 4, 5]), 5)
        self.assertEqual(pos_count([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(pos_count([0, 1, 2, 3, 4]), 5)
        self.assertEqual(pos_count([-1, 0, 1, 2, 3]), 3)
        self.assertEqual(pos_count([-1, -2, -3, 0, 1]), 2)
        self.assertEqual(pos_count([-1, -2, -3, -4, -5, -6]), 0)
