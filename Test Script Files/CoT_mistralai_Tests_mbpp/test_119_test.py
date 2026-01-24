import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(search([1, 2, 3, 4, 5]), 15)
        self.assertEqual(search([10, 20, 30, 40, 50]), 145)
        self.assertEqual(search([-1, 0, 1, 2, 3]), -1)

    def test_edge_cases(self):
        self.assertEqual(search([0]), 0)
        self.assertEqual(search([1]), 1)
        self.assertEqual(search([1, 0]), 1)
        self.assertEqual(search([0, 0]), 0)

    def test_empty_list(self):
        self.assertIsNone(search([]))

    def test_single_element(self):
        self.assertEqual(search([1]), 1)
        self.assertEqual(search([-1]), -1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, search, 'string', 1)
        self.assertRaises(TypeError, search, [1, 2, 3], 'number')
