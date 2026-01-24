import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_maximum_segments_1(self):
        self.assertEqual(maximum_segments(5, 2, 3, 4), 3)

    def test_maximum_segments_2(self):
        self.assertEqual(maximum_segments(10, 1, 2, 3), 4)

    def test_maximum_segments_3(self):
        self.assertEqual(maximum_segments(7, 3, 2, 1), 3)

    def test_maximum_segments_4(self):
        self.assertEqual(maximum_segments(15, 5, 3, 2), 5)

    def test_maximum_segments_5(self):
        self.assertEqual(maximum_segments(20, 10, 5, 3), 6)

    def test_maximum_segments_6(self):
        self.assertEqual(maximum_segments(1, 1, 1, 1), 1)

    def test_maximum_segments_7(self):
        self.assertEqual(maximum_segments(3, 1, 1, 1), 2)

    def test_maximum_segments_8(self):
        self.assertEqual(maximum_segments(4, 2, 1, 1), 2)

    def test_maximum_segments_9(self):
        self.assertEqual(maximum_segments(5, 3, 2, 1), 3)

    def test_maximum_segments_10(self):
        self.assertEqual(maximum_segments(6, 4, 3, 2), 4)
