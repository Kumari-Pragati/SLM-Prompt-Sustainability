import unittest
from mbpp_338_code import count_Substring_With_Equal_Ends

class TestCountSubstringWithEqualEnds(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aba"), 2)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends(""), 0)

    def test_edge_case_single_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_edge_case_single_character_string2(self):
        self.assertEqual(count_Substring_With_Equal_Ends("a"), 1)

    def test_edge_case_two_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ab"), 1)

    def test_edge_case_two_character_string2(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ba"), 1)

    def test_edge_case_three_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("aba"), 2)

    def test_edge_case_three_character_string2(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 1)

    def test_edge_case_three_character_string3(self):
        self.assertEqual(count_Substring_With_Equal_Ends("bac"), 1)

    def test_edge_case_three_character_string4(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abc"), 1)

    def test_edge_case_four_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abab"), 2)

    def test_edge_case_four_character_string2(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abac"), 1)

    def test_edge_case_four_character_string3(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcd"), 1)

    def test_edge_case_four_character_string4(self):
        self.assertEqual(count_Substring_With_Equal_Ends("dcba"), 1)

    def test_edge_case_five_character_string(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababa"), 2)

    def test_edge_case_five_character_string2(self):
        self.assertEqual(count_Substring_With_Equal_Ends("ababc"), 1)

    def test_edge_case_five_character_string3(self):
        self.assertEqual(count_Substring_With_Equal_Ends("abcda"), 1)

    def test_edge_case_five_character_string4(self):
        self.assertEqual(count_Substring_With_Equal_Ends("dcbad"), 1)

    def test_edge_case_five_character_string5(self):
        self.assertEqual(count_Substring_With_Equal_Ends("badca"), 1)

    def test_edge_case_five_character_string6(self):
        self.assertEqual(count_Substring_With_Equal_Ends("dcabc"), 1)

    def test_edge_case_five_character_string7(self):
        self.assertEqual(count_Substring_With_Equal_Ends("badcb"), 1)

    def test_edge_case_five_character_string8(self):
        self.assertEqual(count_Substring_With_Equal_Ends("dcbaa"), 2)

    def test_edge_case_five_character_string9(self):
        self.assertEqual(count_Substring_With_Equal_Ends("badab"), 1)

    def test_edge_case_five_character_string10(self):
        self.assertEqual(count_Substring_With_Equal_Ends("dcaba"), 1)

    def test_edge_case_five_character_string11(self):
        self.assertEqual(count_Substring_With_Equal_Ends("badac"), 1)

    def test_edge_case_five_character_string12(self):
        self.assertEqual(count_Substring_With_Equal_Ends("dcabb"), 1)

    def test_edge_case_five_character_string13(self):
        self.assertEqual(count_Substring_With_Equal_Ends("badad"), 1)

    def test_edge_case_five_character_string14(self):
        self.assertEqual(count_Substring_With_Equal_Ends("dcabc"), 1)

    def test_edge_case_five_character_string15(self):
        self.assertEqual(count_Substring_With_Equal_Ends("badae"), 1)

    def test_edge_case_five_character_string16(self):
        self.assertEqual(count_Substring_With_Equal_Ends("dcabf"), 1)

    def test_edge_case_five_character_string17(self):
        self.assertEqual(count_Substring_With_Equal_Ends("badaf"), 1)

    def test_edge_case_five_character_string18(self):
        self.assertEqual(count_Substring_With_Equal_Ends("dcabg"), 1)

    def test_edge_case_five_character_string19(self):
        self.assertEqual(count_Substring_With_Equal_Ends("badag"), 1)

    def test_edge_case_five_character_string20(self):
        self.assertEqual(count_Substring_With_Equal_Ends("dc