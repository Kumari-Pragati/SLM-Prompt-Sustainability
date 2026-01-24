import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(closest_num(5), 4)

    def test_edge_case(self):
        self.assertEqual(closest_num(1), 0)

    def test_edge_case2(self):
        self.assertEqual(closest_num(0), -1)

    def test_edge_case3(self):
        self.assertEqual(closest_num(-1), -2)

    def test_edge_case4(self):
        self.assertEqual(closest_num(-5), -6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            closest_num('a')
