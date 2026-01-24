import unittest
from mbpp_119_code import search

class TestSearch(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(search([1, 2, 3, 4]), 0)
        self.assertEqual(search([5, 10, 15, 20]), 95)

    def test_edge_cases(self):
        self.assertEqual(search([0]), 0)
        self.assertEqual(search([1]), 0)
        self.assertEqual(search([2, 2, 2]), 0)
        self.assertEqual(search([255, 255, 255]), 0)
        self.assertEqual(search([-1, -1, -1]), 0)

    def test_boundary_conditions(self):
        self.assertEqual(search([1, 2, 3, 4, 5]), 15)
        self.assertEqual(search([10, 20, 30, 40, 50]), 95)
        self.assertEqual(search([255, 255, 255, 255, 255]), 0)
        self.assertEqual(search([-1, -1, -1, -1, -1]), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, search, 1, 2)
        self.assertRaises(TypeError, search, [1, 2, 3], 'n')
