import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(add_K_element([], 3), [])

    def test_single_element(self):
        self.assertListEqual(add_K_element([(1, 2)], 3), [(4, 5)])

    def test_multiple_elements(self):
        self.assertListEqual(add_K_element([((1, 2), (3, 4)), ((5, 6), (7, 8))], 3),
                             [((4, 5), (6, 9)), ((8, 11), (10, 13))])

    def test_negative_K(self):
        self.assertListEqual(add_K_element([((1, 2), (3, 4)), ((5, 6), (7, 8))], -2),
                             [((-1, -2), (-3, -4)), ((-5, -6), (-7, -8))])
