import unittest
from mbpp_172_code import count_occurance

class TestCountOcurance(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_occurance("std"), 1)

    def test_edge_case(self):
        self.assertEqual(count_occurance("stda"), 1)
        self.assertEqual(count_occurance("stdb"), 1)
        self.assertEqual(count_occurance("stdc"), 1)

    def test_edge_case2(self):
        self.assertEqual(count_occurance("stdx"), 0)
        self.assertEqual(count_occurance("stdy"), 0)
        self.assertEqual(count_occurance("stdz"), 0)

    def test_edge_case3(self):
        self.assertEqual(count_occurance("st"), 0)
        self.assertEqual(count_occurance("std"), 1)
        self.assertEqual(count_occurance("stda"), 1)

    def test_edge_case4(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case5(self):
        self.assertEqual(count_occurance(""), 0)
        self.assertEqual(count_occurance("st"), 0)
        self.assertEqual(count_occurance("std"), 1)

    def test_edge_case6(self):
        self.assertEqual(count_occurance("stddaa"), 1)
        self.assertEqual(count_occurance("stddab"), 1)
        self.assertEqual(count_occurance("stddac"), 1)

    def test_edge_case7(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case8(self):
        self.assertEqual(count_occurance("std"), 1)
        self.assertEqual(count_occurance("stda"), 1)
        self.assertEqual(count_occurance("stdb"), 1)

    def test_edge_case9(self):
        self.assertEqual(count_occurance("st"), 0)
        self.assertEqual(count_occurance("std"), 1)
        self.assertEqual(count_occurance("stda"), 1)

    def test_edge_case10(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case11(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case12(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case13(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case14(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case15(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case16(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case17(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case18(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case19(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_occurance("stddd"), 1)
        self.assertEqual(count_occurance("stddaa"), 1)

    def test_edge_case20(self):
        self.assertEqual(count_occurance("stdd"), 1)
        self.assertEqual(count_oc