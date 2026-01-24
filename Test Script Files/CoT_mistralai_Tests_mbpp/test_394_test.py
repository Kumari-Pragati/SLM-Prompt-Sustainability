import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(check_distinct([]))

    def test_single_element(self):
        for element in [1, 'a', (1, 2, 3), frozenset([1, 2, 3])]:
            self.assertTrue(check_distinct([element]))

    def test_multiple_elements(self):
        for elements in [(1, 2, 3), (1, 'a', 3), (1, (1, 2), 3), (1, 2, 'a')]:
            self.assertTrue(check_distinct(elements))

    def test_duplicates(self):
        for elements in [(1, 1, 2), (1, 'a', 'a'), (1, (1, 2), (1, 2)), (1, 1, 'a')]:
            self.assertFalse(check_distinct(elements))

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, check_distinct, 1)
        self.assertRaises(TypeError, check_distinct, '1')
        self.assertRaises(TypeError, check_distinct, (1, '2'))
        self.assertRaises(TypeError, check_distinct, (1, 2, '3'))
        self.assertRaises(TypeError, check_distinct, frozenset([1, '2']))
        self.assertRaises(TypeError, check_distinct, frozenset([1, 2, '3']))
