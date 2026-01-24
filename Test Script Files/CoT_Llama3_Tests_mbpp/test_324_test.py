import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((3, 7)))

    def test_empty_input(self):
        self.assertEqual(sum_of_alternates(()), ((0,), (0,)))

    def test_single_element_input(self):
        self.assertEqual(sum_of_alternates((1,)), ((0,), (1,))

    def test_edge_case_input(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5, 6)), ((3, 12)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_of_alternates("not a tuple")
