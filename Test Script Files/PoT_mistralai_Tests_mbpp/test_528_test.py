import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_length([1, 2, 3, 4, 5]), (1, 1))
        self.assertEqual(min_length([10, 20, 30, 40, 50]), (2, 10))

    def test_empty_list(self):
        self.assertEqual(min_length([]), (0, None))

    def test_single_element_list(self):
        self.assertEqual(min_length([1]), (1, 1))

    def test_negative_numbers(self):
        self.assertEqual(min_length([-1, -2, -3]), (3, -1))

    def test_mixed_types(self):
        self.assertEqual(min_length([1, 'a', 3, 'b']), (2, 1))

    def test_all_same_length(self):
        self.assertEqual(min_length([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), (3, [1, 2, 3]))

    def test_all_same_length_empty(self):
        self.assertEqual(min_length([[], [], []]), (0, None))

    def test_all_same_length_mixed(self):
        self.assertEqual(min_length([[1, 2, 3], [], [1, 2, 3]]), (2, [1, 2, 3]))
