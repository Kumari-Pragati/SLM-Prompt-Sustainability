import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(array_3d(1, 1, 1), [ [ [ '*' ] ] ])

    def test_typical_input(self):
        self.assertEqual(array_3d(2, 2, 2), [ [ [ '*', '*' ], [ '*', '*' ] ], [ [ '*', '*' ], [ '*', '*' ] ], [ [ '*', '*' ], [ '*', '*' ] ] ])

    def test_edge_conditions(self):
        self.assertEqual(array_3d(0, 0, 0), [])
        self.assertEqual(array_3d(0, 1, 1), [ [ [ '*' ] ] ])
        self.assertEqual(array_3d(1, 0, 1), [ [ [ '*' ] ] ])
        self.assertEqual(array_3d(1, 1, 0), [ [ [ '*' ] ] ])

    def test_complex_cases(self):
        self.assertEqual(array_3d(3, 3, 3), [ [ [ '*', '*', '*' ], [ '*', '*', '*' ], [ '*', '*', '*' ] ], [ [ '*', '*', '*' ], [ '*', '*', '*' ], [ '*', '*', '*' ] ], [ [ '*', '*', '*' ], [ '*', '*', '*' ], [ '*', '*', '*' ] ] ])
