import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_single_element_list(self):
        self.assertEqual(position_min([1]), [0])

    def test_multiple_elements_same_value(self):
        self.assertEqual(position_min([1, 1, 2]), [0, 1])

    def test_multiple_elements_different_values(self):
        self.assertEqual(position_min([1, 2, 3]), [0, 1])

    def test_min_at_beginning(self):
        self.assertEqual(position_min([1, 2, 1]), [0, 2])

    def test_min_at_end(self):
        self.assertEqual(position_min([1, 2, 1]), [0, 2])

    def test_min_in_middle(self):
        self.assertEqual(position_min([1, 2, 1]), [0, 2])

    def test_min_not_present(self):
        self.assertEqual(position_min([2, 3, 4]), [])

    def test_list_with_non_numeric_values(self):
        self.assertRaises(TypeError, position_min, ['a', 'b', 'c'])
