import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(position_max([1, 2, 3]), [0])
        self.assertEqual(position_max([5, 5, 5]), [0, 1, 2])
        self.assertEqual(position_max([-1, 0, 1]), [0, 2])

    def test_empty(self):
        self.assertEqual(position_max([]), [])

    def test_single_element(self):
        self.assertEqual(position_max([5]), [0])

    def test_max_at_start(self):
        self.assertEqual(position_max([5, 3, 1]), [0])

    def test_max_at_end(self):
        self.assertEqual(position_max([1, 3, 5]), [2])

    def test_max_in_middle(self):
        self.assertEqual(position_max([1, 5, 3]), [1])

    def test_max_at_start_and_end(self):
        self.assertEqual(position_max([5, 5, 5]), [0, 1, 2])

    def test_max_at_start_and_middle(self):
        self.assertEqual(position_max([5, 3, 5]), [0, 2])

    def test_max_at_end_and_middle(self):
        self.assertEqual(position_max([1, 5, 5]), [1, 2])
