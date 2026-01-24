import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(big_diff([1, 2, 3]), 2)

    def test_single_element(self):
        self.assertEqual(big_diff([5]), 0)

    def test_negative_numbers(self):
        self.assertEqual(big_diff([-10, -5]), 5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            big_diff([])

    def test_identical_elements(self):
        self.assertEqual(big_diff([3, 3, 3]), 0)

    def test_max_at_start(self):
        self.assertEqual(big_diff([10, 2, 3]), 8)

    def test_max_at_end(self):
        self.assertEqual(big_diff([1, 2, 10]), 8)
