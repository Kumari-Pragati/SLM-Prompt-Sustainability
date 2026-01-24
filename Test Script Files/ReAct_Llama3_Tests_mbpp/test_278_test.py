import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_first_elements((1, 2, 3)), 1)

    def test_edge_case(self):
        self.assertEqual(count_first_elements((1, (2, 3), 4)), 1)

    def test_edge_case2(self):
        self.assertEqual(count_first_elements((1, 2, (3, 4))), 2)

    def test_edge_case3(self):
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5))), 3)

    def test_edge_case4(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, (5, 6))), 4)

    def test_edge_case5(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, (6, 7))), 5)

    def test_edge_case6(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, (7, 8))), 6)

    def test_edge_case7(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, (8, 9))), 7)

    def test_edge_case8(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, (9, 10))), 8)

    def test_edge_case9(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, (10, 11))), 9)

    def test_edge_case10(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, (11, 12))), 10)

    def test_edge_case11(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, (12, 13))), 11)

    def test_edge_case12(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, (13, 14))), 12)

    def test_edge_case13(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, (14, 15))), 13)

    def test_edge_case14(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, (15, 16))), 14)

    def test_edge_case15(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, (16, 17))), 15)

    def test_edge_case16(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, (17, 18))), 16)

    def test_edge_case17(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, (18, 19))), 17)

    def test_edge_case18(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, (19, 20))), 18)

    def test_edge_case19(self):
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,