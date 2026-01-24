import unittest
from mbpp_860_code import check_alphanumeric

class TestCheckAlphanumeric(unittest.TestCase):
    def test_typical_accept(self):
        self.assertEqual(check_alphanumeric("hello123"), "Accept")

    def test_typical_discard(self):
        self.assertEqual(check_alphanumeric("hello world"), "Discard")

    def test_edge_accept(self):
        self.assertEqual(check_alphanumeric("hello"), "Accept")

    def test_edge_discard(self):
        self.assertEqual(check_alphanumeric("hello world123"), "Discard")

    def test_edge_empty(self):
        self.assertEqual(check_alphanumeric(""), "Discard")

    def test_edge_single_char(self):
        self.assertEqual(check_alphanumeric("a"), "Accept")

    def test_edge_single_char_space(self):
        self.assertEqual(check_alphanumeric(" "), "Discard")

    def test_edge_single_char_non_alphanumeric(self):
        self.assertEqual(check_alphanumeric("!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space(self):
        self.assertEqual(check_alphanumeric("! "), "Discard")

    def test_edge_single_char_non_alphanumeric_space2(self):
        self.assertEqual(check_alphanumeric("!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space3(self):
        self.assertEqual(check_alphanumeric("! "), "Discard")

    def test_edge_single_char_non_alphanumeric_space4(self):
        self.assertEqual(check_alphanumeric("!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space5(self):
        self.assertEqual(check_alphanumeric("!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space6(self):
        self.assertEqual(check_alphanumeric("!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space7(self):
        self.assertEqual(check_alphanumeric("!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space8(self):
        self.assertEqual(check_alphanumeric("!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space9(self):
        self.assertEqual(check_alphanumeric("!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space10(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space11(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space12(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space13(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space14(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space15(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space16(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space17(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space18(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space19(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space20(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space21(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space22(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space23(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!!!!!!!!!!!!"), "Discard")

    def test_edge_single_char_non_alphanumeric_space24(self):
        self.assertEqual(check_alphanumeric("!!!!!!!!!!