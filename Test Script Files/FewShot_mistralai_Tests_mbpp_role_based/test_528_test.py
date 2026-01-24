import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):
    def test_min_length_positive(self):
        self.assertEqual(min_length([1, 2, 3, 4, 5]), (1, 1))
        self.assertEqual(min_length([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), (1, [1, 2, 3]))

    def test_min_length_empty_list(self):
        self.assertEqual(min_length([]), (0, None))

    def test_min_length_single_element(self):
        self.assertEqual(min_length([1]), (1, 1))

    def test_min_length_negative(self):
        self.assertEqual(min_length([-1, -2, -3]), (3, -3))

    def test_min_length_mixed_types(self):
        self.assertEqual(min_length([1, 2, "3", [4, 5]]), (1, 1))
