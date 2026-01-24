import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):

    def test_position_max(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5]), [4])
        self.assertEqual(position_max([-1, -2, -3, -4, -5]), [-1])
        self.assertEqual(position_max([5, 5, 5, 5, 5]), [0, 1, 2, 3, 4])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6]), [5])
        self.assertEqual(position_max([1, 1, 1, 1, 1]), [0, 1, 2, 3, 4])
        self.assertEqual(position_max([-1, -1, -1, -1, -1]), [0, 1, 2, 3, 4])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), [9])
        self.assertEqual(position_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]), [9])
        self.assertEqual(position_max([1, 2, 3,