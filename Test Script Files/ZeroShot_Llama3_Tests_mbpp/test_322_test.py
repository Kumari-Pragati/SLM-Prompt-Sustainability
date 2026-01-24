import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_position_min(self):
        self.assertEqual(position_min([1, 2, 3, 4, 5]), [0, 1, 2, 3, 4])
        self.assertEqual(position_min([-1, -2, -3, -4, -5]), [0, 1, 2, 3, 4])
        self.assertEqual(position_min([5, 5, 5, 5, 5]), [0, 1, 2, 3, 4])
        self.assertEqual(position_min([1, 2, 3, 4, 5, 6]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(position_min([-1, -2, -3, -4, -5, -6]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(position_min([1, 2, 3, 4, 5, 6, 7]), [0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(position_min([-1, -2, -3, -4, -5, -6, -7]), [0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(position_min([1, 2, 3, 4, 5, 6, 7, 8]), [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(position_min([-1, -2, -3, -4, -5, -6, -7, -8]), [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(position_min([1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(position_min([-1, -2, -3, -4, -5, -6, -7, -8, -9]), [0, 1, 2, 3, 4, 5, 6, 7, 8])
