import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_single_element_list(self):
        self.assertEqual(position_min([1]), [0])

    def test_multiple_elements_list(self):
        self.assertEqual(position_min([1, 2, 1, 3, 2, 1]), [0, 3, 4])

    def test_min_not_unique(self):
        self.assertEqual(position_min([1, 2, 1, 1, 3, 2, 1]), [0, 3, 4, 5])

    def test_list_with_non_numeric_values(self):
        self.assertEqual(position_min(['a', 1, 'b', 2, 'c']), [1, 3])
