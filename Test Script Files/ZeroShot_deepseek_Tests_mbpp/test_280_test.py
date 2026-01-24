import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):

    def test_item_in_list(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 3)[0])
        self.assertTrue(sequential_search(['a', 'b', 'c', 'd', 'e'], 'c')[0])
        self.assertTrue(sequential_search([1.1, 2.2, 3.3, 4.4, 5.5], 3.3)[0])

    def test_item_not_in_list(self):
        self.assertFalse(sequential_search([1, 2, 3, 4, 5], 6)[0])
        self.assertFalse(sequential_search(['a', 'b', 'c', 'd', 'e'], 'f')[0])
        self.assertFalse(sequential_search([1.1, 2.2, 3.3, 4.4, 5.5], 6.6)[0])

    def test_position(self):
        self.assertEqual(sequential_search([1, 2, 3, 4, 5], 3)[1], 2)
        self.assertEqual(sequential_search(['a', 'b', 'c', 'd', 'e'], 'c')[1], 2)
        self.assertEqual(sequential_search([1.1, 2.2, 3.3, 4.4, 5.5], 3.3)[1], 2)
