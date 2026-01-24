import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 2, 4), [3, 4])
        self.assertEqual(remove_list_range([10, 20, 30, 40, 50], 20, 40), [20, 30, 40])
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 1, 5), [1, 2, 3, 4, 5])

    def test_edge_cases(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 1, 1), [1])
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 5, 5), [5])
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 0, 0), [])

    def test_special_cases(self):
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], 0, 10), [1, 2, 3, 4, 5])
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], -1, 10), [1, 2, 3, 4, 5])
        self.assertEqual(remove_list_range([1, 2, 3, 4, 5], -1, -10), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            remove_list_range(None, 1, 2)
        with self.assertRaises(TypeError):
            remove_list_range([1, 2, 3, 4, 5], None, 2)
        with self.assertRaises(TypeError):
            remove_list_range([1, 2, 3, 4, 5], 1, None)
