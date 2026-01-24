import unittest
from mbpp_554_code import Split

class TestSplit(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_input(self):
        self.assertEqual(Split([]), [])

    def test_all_even_input(self):
        self.assertEqual(Split([2, 4, 6]), [])

    def test_all_odd_input(self):
        self.assertEqual(Split([1, 3, 5]), [1, 3, 5])

    def test_mixed_input(self):
        self.assertEqual(Split([1, 2, 3, 4, 5, 6]), [1, 3, 5])
