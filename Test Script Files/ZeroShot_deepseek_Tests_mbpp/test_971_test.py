import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_maximum_segments(self):
        self.assertEqual(maximum_segments(5, 1, 2, 3), 3)
        self.assertEqual(maximum_segments(10, 2, 3, 4), 4)
        self.assertEqual(maximum_segments(15, 5, 7, 9), 4)
        self.assertEqual(maximum_segments(20, 10, 15, 20), 5)
        self.assertEqual(maximum_segments(0, 1, 2, 3), 0)
