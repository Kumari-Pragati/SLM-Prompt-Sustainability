import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])

    def test_single_element_list(self):
        self.assertEqual(two_unique_nums([1]), [])

    def test_two_unique_elements(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5]), [1, 2])

    def test_three_unique_elements(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5, 6]), [1, 2, 3])

    def test_duplicates(self):
        self.assertEqual(two_unique_nums([1, 1, 2, 2, 3, 3]), [1, 2])

    def test_all_duplicates(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 1, 1]), [])
