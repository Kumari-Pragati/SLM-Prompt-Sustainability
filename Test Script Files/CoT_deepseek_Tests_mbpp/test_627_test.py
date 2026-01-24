import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5, 6, 7, 8], 0, 8), 9)

    def test_single_element(self):
        self.assertEqual(find_First_Missing([0], 0, 0), 1)

    def test_empty_array(self):
        self.assertEqual(find_First_Missing([], 0, -1), 0)

    def test_missing_first_element(self):
        self.assertEqual(find_First_Missing([1, 2, 3, 4, 5], 0, 4), 0)

    def test_missing_last_element(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 3, 4, 5], 0, 5), 6)

    def test_missing_middle_element(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 4, 5], 0, 4), 3)

    def test_duplicate_elements(self):
        self.assertEqual(find_First_Missing([0, 1, 2, 2, 3, 4, 5], 0, 6), 6)

    def test_negative_numbers(self):
        self.assertEqual(find_First_Missing([-1, 0, 1, 2, 3, 4, 5], 0, 6), -1)

    def test_large_numbers(self):
        self.assertEqual(find_First_Missing([10**6, 10**7, 10**8, 10**9], 0, 3), 10**6 + 1)
