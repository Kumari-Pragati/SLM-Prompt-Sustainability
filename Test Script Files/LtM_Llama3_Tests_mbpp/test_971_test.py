import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(maximum_segments(0, 1, 2, 3), 0)
        self.assertEqual(maximum_segments(1, 1, 2, 3), 1)
        self.assertEqual(maximum_segments(2, 1, 2, 3), 1)
        self.assertEqual(maximum_segments(3, 1, 2, 3), 1)

    def test_edge(self):
        self.assertEqual(maximum_segments(4, 1, 2, 3), 1)
        self.assertEqual(maximum_segments(5, 1, 2, 3), 1)
        self.assertEqual(maximum_segments(6, 1, 2, 3), 1)
        self.assertEqual(maximum_segments(7, 1, 2, 3), 1)

    def test_complex(self):
        self.assertEqual(maximum_segments(10, 1, 2, 3), 2)
        self.assertEqual(maximum_segments(11, 1, 2, 3), 2)
        self.assertEqual(maximum_segments(12, 1, 2, 3), 2)
        self.assertEqual(maximum_segments(13, 1, 2, 3), 2)
