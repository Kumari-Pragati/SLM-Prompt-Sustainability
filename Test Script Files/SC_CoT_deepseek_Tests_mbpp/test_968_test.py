import unittest

from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(floor_Max(2,3,4), 2)

    def test_boundary_case(self):
        self.assertEqual(floor_Max(2,3,3), 1)
        self.assertEqual(floor_Max(2,3,2), 1)

    def test_edge_case(self):
        self.assertEqual(floor_Max(2,3,1), 0)
        self.assertEqual(floor_Max(2,3,0), 0)
        self.assertEqual(floor_Max(2,3,-1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            floor_Max('2',3,4)
        with self.assertRaises(TypeError):
            floor_Max(2,'3',4)
        with self.assertRaises(TypeError):
            floor_Max(2,3,'4')
        with self.assertRaises(TypeError):
            floor_Max(2,3,4.5)
        with self.assertRaises(TypeError):
            floor_Max(2.5,3,4)
        with self.assertRaises(TypeError):
            floor_Max(2,3.5,4)
