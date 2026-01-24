import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):

    def test_search_function(self):
        self.assertEqual(search([1, 2, 3, 4, 5, 6], 6), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7], 7), 1)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8], 8), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 21), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 22), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 23), 0)
        self.assertEqual(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,