import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):
    def test_positive_list(self):
        self.assertIsNone(neg_nos([1, 2, 3]))

    def test_negative_list(self):
        self.assertEqual(neg_nos([-1, 0, 2]), -1)

    def test_single_negative_number(self):
        self.assertEqual(neg_nos([-1]), -1)

    def test_single_positive_number(self):
        self.assertIsNone(neg_nos([1]))

    def test_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_list_with_zero(self):
        self.assertIsNone(neg_nos([0]))

    def test_negative_and_positive_numbers(self):
        self.assertEqual(neg_nos([-1, 1, 2]), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            neg_nos("not a number")
