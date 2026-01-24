import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_equal_intervals(self):
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, -1))

    def test_non_equal_intervals(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (1, 4))

    def test_non_equal_intervals_reverse(self):
        self.assertEqual(find_Points(4, 3, 2, 1), (2, 4))

    def test_non_equal_intervals_reverse2(self):
        self.assertEqual(find_Points(3, 2, 1, 4), (1, 4))

    def test_non_equal_intervals_reverse3(self):
        self.assertEqual(find_Points(2, 1, 4, 3), (2, 4))

    def test_non_equal_intervals_reverse4(self):
        self.assertEqual(find_Points(1, 4, 2, 3), (1, 4))

    def test_non_equal_intervals_reverse5(self):
        self.assertEqual(find_Points(4, 1, 3, 2), (2, 4))

    def test_non_equal_intervals_reverse6(self):
        self.assertEqual(find_Points(3, 4, 2, 1), (1, 4))

    def test_non_equal_intervals_reverse7(self):
        self.assertEqual(find_Points(2, 3, 1, 4), (1, 4))

    def test_non_equal_intervals_reverse8(self):
        self.assertEqual(find_Points(1, 3, 2, 4), (1, 4))

    def test_non_equal_intervals_reverse9(self):
        self.assertEqual(find_Points(4, 2, 3, 1), (1, 4))

    def test_non_equal_intervals_reverse10(self):
        self.assertEqual(find_Points(3, 2, 4, 1), (1, 4))
