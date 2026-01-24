import unittest
from mbpp_603_code import get_ludic

class TestGetLudic(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case_n_1(self):
        self.assertEqual(get_ludic(1), [1])

    def test_edge_case_n_2(self):
        self.assertEqual(get_ludic(2), [1, 2])

    def test_edge_case_n_3(self):
        self.assertEqual(get_ludic(3), [1, 2, 3])

    def test_edge_case_n_4(self):
        self.assertEqual(get_ludic(4), [1, 2, 3, 4])

    def test_edge_case_n_5(self):
        self.assertEqual(get_ludic(5), [1, 2, 3, 4, 5])

    def test_edge_case_n_6(self):
        self.assertEqual(get_ludic(6), [1, 2, 3, 4, 5, 6])

    def test_edge_case_n_7(self):
        self.assertEqual(get_ludic(7), [1, 2, 3, 4, 5, 6, 7])

    def test_edge_case_n_8(self):
        self.assertEqual(get_ludic(8), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_edge_case_n_9(self):
        self.assertEqual(get_ludic(9), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_n_10(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case_n_11(self):
        self.assertEqual(get_ludic(11), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_edge_case_n_12(self):
        self.assertEqual(get_ludic(12), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_edge_case_n_13(self):
        self.assertEqual(get_ludic(13), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_edge_case_n_14(self):
        self.assertEqual(get_ludic(14), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_edge_case_n_15(self):
        self.assertEqual(get_ludic(15), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_ludic('a')
