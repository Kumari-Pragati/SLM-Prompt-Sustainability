import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_insert_element_typical(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4])

    def test_insert_element_edge(self):
        self.assertEqual(insert_element([], 4), [4])

    def test_insert_element_edge2(self):
        self.assertEqual(insert_element([1], 2), [1, 2])

    def test_insert_element_edge3(self):
        self.assertEqual(insert_element([1, 2, 3], 1), [1, 2, 3, 1])

    def test_insert_element_edge4(self):
        self.assertEqual(insert_element([1, 2, 3], 3), [1, 2, 3, 3])

    def test_insert_element_edge5(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 3, 4])

    def test_insert_element_edge6(self):
        self.assertEqual(insert_element([1, 2, 3], 5), [1, 2, 3, 5])

    def test_insert_element_edge7(self):
        self.assertEqual(insert_element([1, 2, 3], 6), [1, 2, 3, 6])

    def test_insert_element_edge8(self):
        self.assertEqual(insert_element([1, 2, 3], 7), [1, 2, 3, 7])

    def test_insert_element_edge9(self):
        self.assertEqual(insert_element([1, 2, 3], 8), [1, 2, 3, 8])

    def test_insert_element_edge10(self):
        self.assertEqual(insert_element([1, 2, 3], 9), [1, 2, 3, 9])

    def test_insert_element_edge11(self):
        self.assertEqual(insert_element([1, 2, 3], 10), [1, 2, 3, 10])

    def test_insert_element_edge12(self):
        self.assertEqual(insert_element([1, 2, 3], 11), [1, 2, 3, 11])

    def test_insert_element_edge13(self):
        self.assertEqual(insert_element([1, 2, 3], 12), [1, 2, 3, 12])

    def test_insert_element_edge14(self):
        self.assertEqual(insert_element([1, 2, 3], 13), [1, 2, 3, 13])

    def test_insert_element_edge15(self):
        self.assertEqual(insert_element([1, 2, 3], 14), [1, 2, 3, 14])

    def test_insert_element_edge16(self):
        self.assertEqual(insert_element([1, 2, 3], 15), [1, 2, 3, 15])

    def test_insert_element_edge17(self):
        self.assertEqual(insert_element([1, 2, 3], 16), [1, 2, 3, 16])

    def test_insert_element_edge18(self):
        self.assertEqual(insert_element([1, 2, 3], 17), [1, 2, 3, 17])

    def test_insert_element_edge19(self):
        self.assertEqual(insert_element([1, 2, 3], 18), [1, 2, 3, 18])

    def test_insert_element_edge20(self):
        self.assertEqual(insert_element([1, 2, 3], 19), [1, 2, 3, 19])

    def test_insert_element_edge21(self):
        self.assertEqual(insert_element([1, 2, 3], 20), [1, 2, 3, 20])

    def test_insert_element_edge22(self):
        self.assertEqual(insert_element([1, 2, 3], 21), [1, 2, 3, 21])

    def test_insert_element_edge23(self):
        self.assertEqual(insert_element([1, 2, 3], 22), [1, 2, 3, 22])

    def test_insert_element_edge24(self):
        self.assertEqual(insert_element([1, 2, 3], 23), [1, 2, 3, 23])

    def test_insert_element_edge25(self):
        self.assertEqual(insert_element([1, 2, 3], 24), [1, 2, 3, 24])

    def test_insert_element_edge26(self):
        self.assertEqual(insert_element([1, 2, 3], 25), [1, 2, 3, 25])

    def test_insert_element_edge27(self