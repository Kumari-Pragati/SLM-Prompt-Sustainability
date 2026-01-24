import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(Diff([1,2,3,4,5],[2,3,4]), [1,5])

    def test_empty(self):
        self.assertEqual(Diff([],[]), [])

    def test_single_list(self):
        self.assertEqual(Diff([1,2,3],[1,2,3]), [])

    def test_duplicates(self):
        self.assertEqual(Diff([1,1,2,2,3],[2,2,3]), [1,1])

    def test_duplicates2(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5]), [])

    def test_duplicates3(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6]), [6])

    def test_duplicates4(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7]), [6,7])

    def test_duplicates5(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8]), [6,7,8])

    def test_duplicates6(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8,9]), [6,7,8,9])

    def test_duplicates7(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10]), [6,7,8,9,10])

    def test_duplicates8(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11]), [6,7,8,9,10,11])

    def test_duplicates9(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12]), [6,7,8,9,10,11,12])

    def test_duplicates10(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13]), [6,7,8,9,10,11,12,13])

    def test_duplicates11(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14]), [6,7,8,9,10,11,12,13,14])

    def test_duplicates12(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]), [6,7,8,9,10,11,12,13,14,15])

    def test_duplicates13(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]), [6,7,8,9,10,11,12,13,14,15,16])

    def test_duplicates14(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]), [6,7,8,9,10,11,12,13,14,15,16,17])

    def test_duplicates15(self):
        self.assertEqual(Diff([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]), [6,7,8,9,10,11,12,13,14,15,16,17,18])
