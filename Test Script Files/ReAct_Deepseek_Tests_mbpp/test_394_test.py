import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_distinct((1, 2, 3, 4, 5)))

    def test_empty_tuple(self):
        self.assertTrue(check_distinct(()))

    def test_single_element_tuple(self):
        self.assertTrue(check_distinct((1,)))

    def test_duplicate_elements(self):
        self.assertFalse(check_distinct((1, 2, 2, 3)))

    def test_large_number_of_elements(self):
        self.assertTrue(check_distinct(tuple(range(1, 10001))))

    def test_large_number_of_duplicates(self):
        self.assertFalse(check_distinct(tuple(range(1, 10001)) + (1,)))
