import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(check_distinct([]))

    def test_single_element(self):
        self.assertTrue(check_distinct([1]))

    def test_duplicate_elements(self):
        self.assertFalse(check_distinct([1, 1]))
        self.assertFalse(check_distinct([1, '1']))
        self.assertFalse(check_distinct([1, 1.0]))

    def test_mixed_types(self):
        self.assertFalse(check_distinct([1, 'a', 3.14]))

    def test_multiple_unique_elements(self):
        self.assertTrue(check_distinct([1, 2, 3]))
        self.assertTrue(check_distinct([1, 'a', 3.14]))
        self.assertTrue(check_distinct([1, 2, 'a', 3.14]))
        self.assertTrue(check_distinct([1, 'a', 3.14, 1]))
