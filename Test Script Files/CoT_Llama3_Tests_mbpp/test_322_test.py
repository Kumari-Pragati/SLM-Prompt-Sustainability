import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_position_min_single_element(self):
        self.assertEqual(position_min([1]), [0])

    def test_position_min_multiple_elements(self):
        self.assertEqual(position_min([1, 2, 3, 2, 1]), [0, 3, 4])

    def test_position_min_multiple_min_elements(self):
        self.assertEqual(position_min([1, 2, 2, 3, 1]), [1, 2, 3, 4])

    def test_position_min_empty_list(self):
        with self.assertRaises(IndexError):
            position_min([])

    def test_position_min_single_element_list(self):
        self.assertEqual(position_min([1]), [0])

    def test_position_min_list_with_duplicates(self):
        self.assertEqual(position_min([1, 2, 2, 3, 1, 2]), [0, 1, 2, 3, 4, 5])
