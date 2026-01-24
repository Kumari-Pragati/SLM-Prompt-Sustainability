import unittest
from mbpp_971_code import maximum_segments

class TestMaximumSegments(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(maximum_segments(10, 2, 3, 4), 4)

    def test_boundary_case(self):
        self.assertEqual(maximum_segments(0, 1, 1, 1), 0)

    def test_edge_case(self):
        self.assertEqual(maximum_segments(15, 5, 6, 7), 4)

    def test_error_case(self):
        with self.assertRaises(TypeError):
            maximum_segments("10", 2, 3, 4)
