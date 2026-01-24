import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_adverbs("I love playing basketball"), "0-12: love")

    def test_edge_case(self):
        self.assertEqual(find_adverbs(""), "")

    def test_edge_case2(self):
        self.assertEqual(find_adverbs("I am happy"), "")

    def test_edge_case3(self):
        self.assertEqual(find_adverbs("I am"), "")

    def test_edge_case4(self):
        self.assertEqual(find_adverbs("I am not happy"), "")

    def test_edge_case5(self):
        self.assertEqual(find_adverbs("I am not"), "")

    def test_edge_case6(self):
        self.assertEqual(find_adverbs("I am not very happy"), "12-24: not very")

    def test_edge_case7(self):
        self.assertEqual(find_adverbs("I am not very"), "")

    def test_edge_case8(self):
        self.assertEqual(find_adverbs("I am not very happy today"), "12-24: not very")

    def test_edge_case9(self):
        self.assertEqual(find_adverbs("I am not very happy today I am not very"), "12-24: not very")

    def test_edge_case10(self):
        self.assertEqual(find_adverts("I am not very happy today I am not very"), "")

    def test_edge_case11(self):
        self.assertEqual(find_adverts("I am not very happy today I am not very happy"), "12-24: not very")

    def test_edge_case12(self):
        self.assertEqual(find_adverts("I am not very happy today I am not very happy today"), "12-24: not very")

    def test_edge_case13(self):
        self.assertEqual(find_adverts("I am not very happy today I am not very happy today I am not very"), "12-24: not very")

    def test_edge_case14(self):
        self.assertEqual(find_adverts("I am not very happy today I am not very happy today I am not very happy"), "12-24: not very")

    def test_edge_case15(self):
        self.assertEqual(find_adverts("I am not very happy today I am not very happy today I am not very happy today"), "12-24: not very")
