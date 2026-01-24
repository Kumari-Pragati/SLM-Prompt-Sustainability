import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 3), [1, 2, 3, 5])

    def test_edge_case(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 1), [1, 2, 3, 4])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])

    def test_edge_case2(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_kth_element('abc', 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            remove_kth_element([1, 2, 3], 'a')
