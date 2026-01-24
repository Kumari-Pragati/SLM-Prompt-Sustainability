import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(position_min([1, 2, 3, 4, 5]), [0, 1, 2, 3, 4])
        self.assertEqual(position_min([-1, -2, -3, -4, -5]), [0, 1, 2, 3, 4])
        self.assertEqual(position_min([5, 5, 5, 5, 5]), [0, 1, 2, 3, 4])

    def test_empty(self):
        self.assertEqual(position_min([]), [])

    def test_single_element(self):
        self.assertEqual(position_min([1]), [0])

    def test_multiple_min(self):
        self.assertEqual(position_min([1, 2, 2, 3, 4]), [0, 2, 3])

    def test_negative_min(self):
        self.assertEqual(position_min([-1, -2, -3, -4, -5]), [0, 1, 2, 3, 4])

    def test_max_min(self):
        self.assertEqual(position_min([5, 5, 5, 5, 5]), [0, 1, 2, 3, 4])
