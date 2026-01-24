import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):
    def test_remove_kth_element_typical(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 3), [1, 2, 3, 5])

    def test_remove_kth_element_edge(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 1), [1, 2, 3, 4])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])

    def test_remove_kth_element_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_kth_element("string", 3)
        with self.assertRaises(TypeError):
            remove_kth_element([1, 2, 3, 4, 5], "string")

    def test_remove_kth_element_empty_list(self):
        self.assertEqual(remove_kth_element([], 1), [])

    def test_remove_kth_element_single_element(self):
        self.assertEqual(remove_kth_element([1], 1), [])
