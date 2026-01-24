import unittest
from mbpp_6_code import differ_At_OneBitPos

class TestDifferAtOneBitPos(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(differ_At_OneBitPos(5, 6), False)
        self.assertEqual(differ_At_OneBitPos(3, 4), True)
        self.assertEqual(differ_At_OneBitPos(10, 11), True)

    def test_edge_cases(self):
        self.assertEqual(differ_At_OneBitPos(0, 1), False)
        self.assertEqual(differ_At_OneBitPos(1, 0), True)
        self.assertEqual(differ_At_OneBitPos(1, 1), False)
        self.assertEqual(differ_At_OneBitPos(2, 3), True)

    def test_boundary_cases(self):
        self.assertEqual(differ_At_OneBitPos(2**31 - 1, 2**31), True)
        self.assertEqual(differ_At_OneBitPos(2**31, 2**31 + 1), True)
        self.assertEqual(differ_At_OneBitPos(-2**31, -2**31 - 1), True)
        self.assertEqual(differ_At_OneBitPos(-2**31 - 1, -2**31), True)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, differ_At_OneBitPos, "a", 1)
        self.assertRaises(TypeError, differ_At_OneBitPos, 1, "b")
        self.assertRaises(TypeError, differ_At_OneBitPos, None, None)
