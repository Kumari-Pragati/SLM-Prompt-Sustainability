import unittest
from mbpp_105_code import count

class TestCountFunction(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count([1, 2, 3, 4]), 10)

    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_single_element(self):
        self.assertEqual(count([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(count([-1, -2, -3]), -6)

    def test_large_numbers(self):
        self.assertEqual(count([1000000001, 1000000002, 1000000003]), 3000000006)
