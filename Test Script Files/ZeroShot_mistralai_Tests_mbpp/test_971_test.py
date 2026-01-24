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

    def test_two_elements(self):
        self.assertEqual(maximum_segments(2, 0, 0, 0), 2)
        self.assertEqual(maximum_segments(2, 1, 0, 0), 2)
        self.assertEqual(maximum_segments(2, 0, 1, 0), 2)
        self.assertEqual(maximum_segments(2, 0, 0, 1), 2)
        self.assertEqual(maximum_segments(2, 1, 1, 0), 3)
        self.assertEqual(maximum_segments(2, 1, 0, 1), 3)
        self.assertEqual(maximum_segments(2, 0, 1, 1), 3)

    def test_three_elements(self):
        self.assertEqual(maximum_segments(3, 0, 0, 0), 3)
        self.assertEqual(maximum_segments(3, 1, 0, 0), 4)
        self.assertEqual(maximum_segments(3, 0, 1, 0), 4)
        self.assertEqual(maximum_segments(3, 0, 0, 1), 4)
        self.assertEqual(maximum_segments(3, 1, 1, 0), 5)
        self.assertEqual(maximum_segments(3, 1, 0, 1), 5)
        self.assertEqual(maximum_segments(3, 0, 1, 1), 5)
        self.assertEqual(maximum_segments(3, 2, 0, 0), 3)
        self.assertEqual(maximum_segments(3, 0, 2, 0), 3)
        self.assertEqual(maximum_segments(3, 0, 0, 2), 3)
        self.assertEqual(maximum_segments(3, 1, 2, 0), 4)
        self.assertEqual(maximum_segments(3, 1, 0, 2), 4)
        self.assertEqual(maximum_segments(3, 0, 1, 2), 4)
        self.assertEqual(maximum_segments(3, 2, 1, 0), 5)
        self.assertEqual(maximum_segments(3, 2, 0, 1), 5)
        self.assertEqual(maximum_segments(3, 0, 2, 1), 5)
