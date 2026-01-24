import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")

    def test_edge_case_1(self):
        self.assertEqual(capital_words_spaces("helloWorld"), "hello World")

    def test_edge_case_2(self):
        self.assertEqual(capital_words_spaces("HelloWorld123"), "Hello World123")

    def test_edge_case_3(self):
        self.assertEqual(capital_words_spaces("hello123World"), "hello 123 World")

    def test_edge_case_4(self):
        self.assertEqual(capital_words_spaces("Hello123World"), "Hello 123 World")

    def test_edge_case_5(self):
        self.assertEqual(capital_words_spaces("hello123World"), "hello 123 World")

    def test_edge_case_6(self):
        self.assertEqual(capital_words_spaces("Hello123World123"), "Hello 123 World123")

    def test_edge_case_7(self):
        self.assertEqual(capital_words_spaces("hello123World123"), "hello 123 World123")

    def test_edge_case_8(self):
        self.assertEqual(capital_words_spaces("Hello123World123456"), "Hello 123 World123456")

    def test_edge_case_9(self):
        self.assertEqual(capital_words_spaces("hello123World123456"), "hello 123 World123456")

    def test_edge_case_10(self):
        self.assertEqual(capital_words_spaces("Hello123World123456789"), "Hello 123 World123456789")

    def test_edge_case_11(self):
        self.assertEqual(capital_words_spaces("hello123World123456789"), "hello 123 World123456789")

    def test_edge_case_12(self):
        self.assertEqual(capital_words_spaces("Hello123World123456789012"), "Hello 123 World123456789012")

    def test_edge_case_13(self):
        self.assertEqual(capital_words_spaces("hello123World123456789012"), "hello 123 World123456789012")

    def test_edge_case_14(self):
        self.assertEqual(capital_words_spaces("Hello123World123456789012345"), "Hello 123 World123456789012345")

    def test_edge_case_15(self):
        self.assertEqual(capital_words_spaces("hello123World123456789012345"), "hello 123 World123456789012345")

    def test_edge_case_16(self):
        self.assertEqual(capital_words_spaces("Hello123World123456789012345678"), "Hello 123 World123456789012345678")

    def test_edge_case_17(self):
        self.assertEqual(capital_words_spaces("hello123World123456789012345678"), "hello 123 World123456789012345678")

    def test_edge_case_18(self):
        self.assertEqual(capital_words_spaces("Hello123World123456789012345678901"), "Hello 123 World123456789012345678901")

    def test_edge_case_19(self):
        self.assertEqual(capital_words_spaces("hello123World123456789012345678901"), "hello 123 World123456789012345678901")

    def test_edge_case_20(self):
        self.assertEqual(capital_words_spaces("Hello123World123456789012345678901234"), "Hello 123 World123456789012345678901234")

    def test_edge_case_21(self):
        self.assertEqual(capital_words_spaces("hello123World123456789012345678901234"), "hello 123 World123456789012345678901234")

    def test_edge_case_22(self):
        self.assertEqual(capital_words_spaces("Hello123World123456789012345678901234567"), "Hello 123 World123456789012345678901234567")

    def test_edge_case_23(self):
        self.assertEqual(capital_words_spaces("hello123World123456789012345678901234567"), "hello 123 World123456789012345678901234567")

    def test_edge_case_24(self):
        self.assertEqual(capital_words_spaces("Hello123World123456789012345678901234567890"), "Hello 123 World123456789012345678901234567890")

    def test_edge_case_25(self):
        self.assertEqual(capital_words_spaces("hello123World123456789012345678901234567890"), "hello 123 World123456789012345678901234567890")

    def test_edge_case_26(self):
        self.assertEqual(capital_words_spaces("Hello123World123456789012345678901234567890123"), "Hello 123 World123456789012345678901234567890123")

    def test_edge_case_27(self):
        self.assertEqual(capital_words_spaces("hello123World123456789012345678901234567890123"), "hello 123 World123456