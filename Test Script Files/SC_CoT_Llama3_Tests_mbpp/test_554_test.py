import unittest
from mbpp_554_code import Split

class TestSplitFunction(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case(self):
        self.assertEqual(Split([1, 2, 4, 5]), [1, 5])

    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_single_element_list(self):
        self.assertEqual(Split([10]), [])

    def test_all_even_list(self):
        self.assertEqual(Split([2, 4, 6, 8]), [])

    def test_all_odd_list(self):
        self.assertEqual(Split([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_mixed_list(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            Split('abc')
