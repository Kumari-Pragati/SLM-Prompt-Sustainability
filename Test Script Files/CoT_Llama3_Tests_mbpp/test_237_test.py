import unittest
from mbpp_237_code import check_occurences

class TestCheckOccurences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(check_occurences([]), {})

    def test_single_element(self):
        self.assertEqual(check_occurences([1]), {tuple(sorted([1])): 1})

    def test_multiple_elements(self):
        self.assertEqual(check_occurences([1, 2, 3, 2, 1]), {tuple(sorted([1, 2, 3])): 1, tuple(sorted([2, 1])): 1, tuple(sorted([1, 1])): 2})

    def test_duplicates(self):
        self.assertEqual(check_occurences([1, 1, 2, 2, 2, 3, 3, 3, 3]), {tuple(sorted([1, 1])): 2, tuple(sorted([2, 2, 2, 2])): 4, tuple(sorted([3, 3, 3, 3])): 4})

    def test_negative_numbers(self):
        self.assertEqual(check_occurences([-1, -2, -3, -2, -1]), {tuple(sorted([-1, -2, -3])): 1, tuple(sorted([-2, -1])): 1})

    def test_non_integer_numbers(self):
        self.assertEqual(check_occurences([1.0, 2.0, 3.0, 2.0, 1.0]), {tuple(sorted([1.0, 2.0, 3.0])): 1, tuple(sorted([2.0, 1.0])): 1})

    def test_mixed_types(self):
        self.assertEqual(check_occurences([1, 2, 'a', 'b', 'a', 'b']), {tuple(sorted([1, 2])): 1, tuple(sorted(['a', 'b'])): 2})
