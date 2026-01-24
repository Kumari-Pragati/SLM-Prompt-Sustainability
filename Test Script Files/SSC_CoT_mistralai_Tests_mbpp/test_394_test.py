import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(check_distinct((1, 2, 3, 4, 5)))
        self.assertTrue(check_distinct(('a', 'b', 'c', 'd', 'e')))

    def test_edge_cases(self):
        self.assertTrue(check_distinct((1, 1, 2, 3, 4, 5)))
        self.assertTrue(check_distinct(('a', 'a', 'b', 'c', 'd', 'e')))
        self.assertFalse(check_distinct((1, 1, 1, 2, 3, 4, 5)))
        self.assertFalse(check_distinct(('a', 'a', 'a', 'b', 'c', 'd', 'e')))

    def test_empty_input(self):
        self.assertTrue(check_distinct(()))
        self.assertTrue(check_distinct([]))
        self.assertFalse(check_distinct((None,)))
        self.assertFalse(check_distinct([]))

    def test_single_input(self):
        self.assertTrue(check_distinct((1,)))
        self.assertTrue(check_distinct(('a',)))
        self.assertFalse(check_distinct((1, 1)))
        self.assertFalse(check_distinct(('a', 'a')))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_distinct, (1, 2, 3, 'x'))
        self.assertRaises(TypeError, check_distinct, (1, 2, 3, [4, 5]))
