import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_rotation_count([4, 5, 6, 7, 8, 9, 1, 2, 3]), 6)

    def test_edge_case(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9]), 0)

    def test_edge_case2(self):
        self.assertEqual(find_rotation_count([9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_edge_case3(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0)

    def test_edge_case4(self):
        self.assertEqual(find_rotation_count([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_edge_case5(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 0)

    def test_edge_case6(self):
        self.assertEqual(find_rotation_count([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_edge_case7(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 0)

    def test_edge_case8(self):
        self.assertEqual(find_rotation_count([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_edge_case9(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 0)

    def test_edge_case10(self):
        self.assertEqual(find_rotation_count([13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_edge_case11(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 0)

    def test_edge_case12(self):
        self.assertEqual(find_rotation_count([14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_edge_case13(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 0)

    def test_edge_case14(self):
        self.assertEqual(find_rotation_count([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_edge_case15(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 0)

    def test_edge_case16(self):
        self.assertEqual(find_rotation_count([16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_edge_case17(self):
        self.assertEqual(find_rotation_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), 0)

    def test_edge_case18(self):
        self.assertEqual(find_rotation_count([17, 16,