import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):
    def test_single_negative_number(self):
        self.assertEqual(neg_nos([-1]), -1)

    def test_multiple_negative_numbers(self):
        self.assertEqual(neg_nos([-1, -2, -3]), -1)

    def test_no_negative_numbers(self):
        self.assertIsNone(neg_nos([1, 2, 3]))

    def test_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_list_with_mixed_numbers(self):
        self.assertEqual(neg_nos([-1, 0, 2, -3]), -1)

    def test_list_with_no_numbers(self):
        self.assertIsNone(neg_nos(['a', 'b', 'c']))
