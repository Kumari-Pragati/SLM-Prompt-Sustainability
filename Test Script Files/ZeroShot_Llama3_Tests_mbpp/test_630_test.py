import unittest
from mbpp_630_code import get_coordinates

class TestGetCoordinates(unittest.TestCase):

    def test_get_coordinates(self):
        self.assertEqual(get_coordinates((1,)), [(1,)])
        self.assertEqual(get_coordinates((2,)), [(1,),(2,),(0,)])
        self.assertEqual(get_coordinates((3,)), [(1,),(2,),(3,),(0,),(0,),(1,)])
        self.assertEqual(get_coordinates(()), [()])
        self.assertEqual(get_coordinates((1,1)), [(1,),(1,),(0,),(0,),(1,),(1,),(0,),(0,),(1,)])
        self.assertEqual(get_coordinates((2,2)), [(1,),(1,),(0,),(0,),(1,),(1,),(2,),(2,),(0,),(0,),(1,),(1,),(2,),(2,),(0,),(0,),(1,),(1,),(2,)])

    def test_get_coordinates_edge_cases(self):
        self.assertEqual(get_coordinates((0,)), [(0,)])
        self.assertEqual(get_coordinates((1,1)), [(1,),(1,),(0,),(0,),(1,),(1,),(0,),(0,),(1)])
