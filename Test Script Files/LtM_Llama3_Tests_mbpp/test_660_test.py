import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (1, 4))
        self.assertEqual(find_Points(5, 6, 7, 8), (5, 8))
        self.assertEqual(find_Points(10, 20, 30, 40), (10, 40))

    def test_edge_cases(self):
        self.assertEqual(find_Points(1, 1, 2, 2), (-1, -1))
        self.assertEqual(find_Points(1, 2, 1, 2), (-1, -1))
        self.assertEqual(find_Points(1, 2, 2, 1), (-1, -1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Points('a', 2, 3, 4)
        with self.assertRaises(TypeError):
            find_Points(1, 'b', 3, 4)
        with self.assertRaises(TypeError):
            find_Points(1, 2, 'c', 4)
        with self.assertRaises(TypeError):
            find_Points(1, 2, 3, 'd')
