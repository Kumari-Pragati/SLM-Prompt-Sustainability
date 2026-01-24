import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 2), [1, 3, 5])
        self.assertEqual(nth_items(['a', 'b', 'c', 'd', 'e'], 2), ['a', 'c', 'e'])

    def test_edge_cases(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_negative_step(self):
        with self.assertRaises(TypeError):
            nth_items([1, 2, 3, 4, 5], -1)

    def test_non_integer_step(self):
        with self.assertRaises(TypeError):
            nth_items([1, 2, 3, 4, 5], 2.5)

    def test_empty_list(self):
        self.assertEqual(nth_items([], 2), [])

    def test_list_with_one_element(self):
        self.assertEqual(nth_items([1], 1), [1])

    def test_list_with_two_elements(self):
        self.assertEqual(nth_items([1, 2], 1), [1, 2])

    def test_list_with_three_elements(self):
        self.assertEqual(nth_items([1, 2, 3], 1), [1, 2, 3])
