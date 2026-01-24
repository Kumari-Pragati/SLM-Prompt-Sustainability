import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_Points(1, 3, 2, 4), (-1, 4))

    def test_edge_case_l1_l2_equal(self):
        self.assertEqual(find_Points(1, 1, 2, 2), (-1, 2))

    def test_edge_case_r1_r2_equal(self):
        self.assertEqual(find_Points(1, 3, 2, 2), (1, -1))

    def test_edge_case_l1_l2_r1_r2_equal(self):
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, -1))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_Points('a', 3, 2, 4)
