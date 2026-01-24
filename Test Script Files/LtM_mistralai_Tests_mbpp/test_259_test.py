import unittest
from mbpp_259_code import maximize_elements

class TestMaximizeElements(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(maximize_elements((1, 2), (3, 4)), ((3, 4)))
        self.assertEqual(maximize_elements((5, 6), (7, 8)), ((7, 8)))

    def test_edge_cases(self):
        self.assertEqual(maximize_elements((0, 0), (0, 0)), ((0, 0)))
        self.assertEqual(maximize_elements((1000000000, 1), (1, 1000000000)), ((1000000000, 1000000000)))
        self.assertEqual(maximize_elements((-1, -2), (0, 0)), ((0, 0)))

    def test_complex(self):
        self.assertEqual(maximize_elements(((1, 2), (3, 4)), (((5, 6), (7, 8)), ((9, 10), (11, 12)))), (((7, 8), (11, 12)), ((9, 10), (11, 12))))
        self.assertEqual(maximize_elements(((1, 2), (3, 4)), (((-1, -2), (0, 0)), ((9, 10), (11, 12)))), (((0, 0), (9, 10)), ((1, 2), (3, 4))))
