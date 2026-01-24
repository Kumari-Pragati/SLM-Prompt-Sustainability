import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_Points(1,3,2,4), (1,4))
        self.assertEqual(find_Points(5,7,6,8), (5,8))
        self.assertEqual(find_Points(10,12,11,13), (10,13))

    def test_edge_cases(self):
        self.assertEqual(find_Points(1,1,1,1), (-1,-1))
        self.assertEqual(find_Points(1,2,2,1), (-1,-1))
        self.assertEqual(find_Points(1,1,2,2), (-1,-1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Points('a',1,2,3)
        with self.assertRaises(TypeError):
            find_Points(1,'a',2,3)
        with self.assertRaises(TypeError):
            find_Points(1,2,'a',3)
        with self.assertRaises(TypeError):
            find_Points(1,2,3,'a')
