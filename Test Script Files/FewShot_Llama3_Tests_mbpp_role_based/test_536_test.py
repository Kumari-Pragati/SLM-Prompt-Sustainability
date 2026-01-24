import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = nth_items(list1, 2)
        self.assertEqual(result, [1, 3, 5, 7, 9])

    def test_edge_case_start(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = nth_items(list1, 1)
        self.assertEqual(result, list1)

    def test_edge_case_end(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = nth_items(list1, 10)
        self.assertEqual(result, [10])

    def test_invalid_input_type(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        with self.assertRaises(TypeError):
            nth_items(list1, 'a')

    def test_invalid_input_value(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        with self.assertRaises(IndexError):
            nth_items(list1, 0)
