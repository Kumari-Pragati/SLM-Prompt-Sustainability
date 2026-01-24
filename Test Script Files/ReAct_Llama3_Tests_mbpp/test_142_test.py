import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)

    def test_single_element_lists(self):
        self.assertEqual(count_samepair([1], [1], [1]), 1)
        self.assertEqual(count_samepair([1], [2], [1]), 1)
        self.assertEqual(count_samepair([1, 2], [1, 2], [1, 2]), 3)

    def test_multiple_element_lists(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 4], [1, 2, 3]), 2)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 4]), 2)

    def test_lists_with_duplicates(self):
        self.assertEqual(count_samepair([1, 1, 2], [1, 1, 2], [1, 1, 2]), 3)
        self.assertEqual(count_samepair([1, 1, 2], [1, 2, 2], [1, 1, 2]), 2)

    def test_lists_with_no_common_elements(self):
        self.assertEqual(count_samepair([1, 2, 3], [4, 5, 6], [7, 8, 9]), 0)
