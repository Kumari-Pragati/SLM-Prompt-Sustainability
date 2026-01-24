import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):

    def test_empty_tuple(self):
        """Check if function correctly handles empty tuple"""
        self.assertTrue(check_distinct(()))

    def test_single_element_tuple(self):
        """Check if function correctly handles single element tuple"""
        for element in [1, 'a', (1, 2), (1, 2, 3)]:
            self.assertTrue(check_distinct((element,)))

    def test_multiple_elements_unique(self):
        """Check if function correctly handles multiple unique elements"""
        self.assertTrue(check_distinct((1, 2, 3, 4)))
        self.assertTrue(check_distinct(('a', 'b', 'c')))
        self.assertTrue(check_distinct((1.0, 2.0, 3.0)))

    def test_multiple_elements_duplicate(self):
        """Check if function correctly handles multiple duplicate elements"""
        self.assertFalse(check_distinct((1, 1, 2)))
        self.assertFalse(check_distinct(('a', 'a', 'b')))
        self.assertFalse(check_distinct((1.0, 1.0, 2.0)))

    def test_mixed_types(self):
        """Check if function correctly handles mixed types"""
        self.assertFalse(check_distinct((1, 'a', (1, 2))))
        self.assertFalse(check_distinct(('a', 1, (1, 2))))
        self.assertFalse(check_distinct(((1, 2), 'a', 1)))
