import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_position_min_single_min(self):
        self.assertEqual(position_min([5, 4, 3, 2, 1]), [4])

    def test_position_min_multiple_mins(self):
        self.assertEqual(position_min([5, 4, 3, 2, 2]), [3, 4])

    def test_position_min_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_position_min_single_element(self):
        self.assertEqual(position_min([5]), [0])

    def test_position_min_all_same(self):
        self.assertEqual(position_min([1, 1, 1, 1]), [0, 1, 2, 3])
