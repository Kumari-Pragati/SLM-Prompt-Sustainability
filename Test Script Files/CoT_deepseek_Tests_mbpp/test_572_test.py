import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 2, 1]), [3])

    def test_single_element(self):
        self.assertEqual(two_unique_nums([1]), [1])

    def test_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])

    def test_all_unique(self):
        self.assertEqual(two_unique_nums([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 1]), [])

    def test_large_list(self):
        self.assertEqual(two_unique_nums(list(range(1, 1001))), list(range(1, 1001)))

    def test_negative_numbers(self):
        self.assertEqual(two_unique_nums([-1, -2, -3, -2, -1]), [-3])

    def test_mixed_numbers(self):
        self.assertEqual(two_unique_nums([1, -1, 2, -2, 3, -3]), [1, -1, 2, -2, 3, -3])
