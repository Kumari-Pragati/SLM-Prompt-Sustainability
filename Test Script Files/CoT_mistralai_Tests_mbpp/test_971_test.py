import unittest
from971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(maximum_segments(0, 0, 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(maximum_segments(1, 0, 0, 0), 1)
        self.assertEqual(maximum_segments(1, 1, 0, 0), 1)
        self.assertEqual(maximum_segments(1, 0, 1, 0), 1)
        self.assertEqual(maximum_segments(1, 0, 0, 1), 1)

    def test_small_list(self):
        self.assertEqual(maximum_segments(2, 1, 0, 0), 2)
        self.assertEqual(maximum_segments(2, 0, 1, 0), 2)
        self.assertEqual(maximum_segments(2, 0, 0, 1), 2)
        self.assertEqual(maximum_segments(2, 1, 1, 0), 2)
        self.assertEqual(maximum_segments(2, 1, 0, 1), 2)
        self.assertEqual(maximum_segments(2, 0, 1, 1), 2)

    def test_large_list(self):
        self.assertEqual(maximum_segments(10, 1, 2, 3), 10)
        self.assertEqual(maximum_segments(10, 2, 1, 3), 10)
        self.assertEqual(maximum_segments(10, 3, 1, 2), 10)
        self.assertEqual(maximum_segments(10, 1, 3, 2), 10)
        self.assertEqual(maximum_segments(10, 2, 3, 1), 10)
        self.assertEqual(maximum_segments(10, 3, 2, 1), 10)

    def test_large_different_steps(self):
        self.assertEqual(maximum_segments(10, 1, 5, 3), 10)
        self.assertEqual(maximum_segments(10, 5, 1, 3), 10)
        self.assertEqual(maximum_segments(10, 3, 5, 1), 10)
        self.assertEqual(maximum_segments(10, 5, 3, 1), 10)
        self.assertEqual(maximum_segments(10, 1, 3, 5), 10)
        self.assertEqual(maximum_segments(10, 3, 1, 5), 10)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, maximum_segments, -1, 1, 2, 3)
        self.assertRaises(ValueError, maximum_segments, 0, -1, 2, 3)
        self.assertRaises(ValueError, maximum_segments, 0, 1, -2, 3)
        self.assertRaises(ValueError, maximum_segments, 0, 1, 2, -3)
