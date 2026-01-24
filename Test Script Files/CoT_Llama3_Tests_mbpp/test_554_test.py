import unittest
from mbpp_554_code import Split

class TestSplit(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case(self):
        self.assertEqual(Split([2, 4, 6, 8, 10]), [])

    def test_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_single_element(self):
        self.assertEqual(Split([5]), [5])

    def test_all_even(self):
        self.assertEqual(Split([2, 4, 6, 8]), [])

    def test_all_odd(self):
        self.assertEqual(Split([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_mixed(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9])
