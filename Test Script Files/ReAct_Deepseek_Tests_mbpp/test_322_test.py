import unittest
from mbpp_322_code import position_min

class TestPositionMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(position_min([1, 2, 3, 2, 1]), [0, 3])

    def test_single_element(self):
        self.assertEqual(position_min([5]), [0])

    def test_empty_list(self):
        self.assertEqual(position_min([]), [])

    def test_negative_numbers(self):
        self.assertEqual(position_min([-1, -2, -3, -2, -1]), [0, 2])

    def test_duplicate_min_values(self):
        self.assertEqual(position_min([2, 2, 1, 2, 1]), [0, 1, 3])

    def test_large_list(self):
        self.assertEqual(position_min(list(range(100000, 0, -1))), list(range(99999)))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            position_min([1, 'a', 2, 'b', 1])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            position_min("not a list")
