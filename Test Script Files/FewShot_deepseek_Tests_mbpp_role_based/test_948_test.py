import unittest
from mbpp_948_code import get_item

class TestGetItem(unittest.TestCase):
    def test_typical_use_case(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 2
        self.assertEqual(get_item(tup1, index), 3)

    def test_edge_condition(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 0
        self.assertEqual(get_item(tup1, index), 1)

    def test_boundary_condition(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 4
        self.assertEqual(get_item(tup1, index), 5)

    def test_invalid_input(self):
        tup1 = (1, 2, 3, 4, 5)
        index = 'a'
        with self.assertRaises(TypeError):
            get_item(tup1, index)
