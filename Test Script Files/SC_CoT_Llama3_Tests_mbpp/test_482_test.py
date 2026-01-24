import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(match('HelloWorld'), 'Yes')

    def test_edge_case_uppercase(self):
        self.assertEqual(match('HELLO'), 'No')

    def test_edge_case_lowercase(self):
        self.assertEqual(match('hello'), 'No')

    def test_edge_case_mixedcase(self):
        self.assertEqual(match('Hello'), 'No')

    def test_edge_case_empty_string(self):
        self.assertEqual(match(''), 'No')

    def test_edge_case_single_uppercase(self):
        self.assertEqual(match('A'), 'No')

    def test_edge_case_single_lowercase(self):
        self.assertEqual(match('a'), 'No')

    def test_edge_case_single_mixedcase(self):
        self.assertEqual(match('a'), 'No')

    def test_edge_case_multiple_uppercase(self):
        self.assertEqual(match('ABC'), 'No')

    def test_edge_case_multiple_lowercase(self):
        self.assertEqual(match('abc'), 'No')

    def test_edge_case_multiple_mixedcase(self):
        self.assertEqual(match('AbC'), 'No')

    def test_edge_case_multiple_mixedcase2(self):
        self.assertEqual(match('AbCdef'), 'No')

    def test_edge_case_multiple_mixedcase3(self):
        self.assertEqual(match('AbCdefgh'), 'No')

    def test_edge_case_multiple_mixedcase4(self):
        self.assertEqual(match('AbCdefghij'), 'No')

    def test_edge_case_multiple_mixedcase5(self):
        self.assertEqual(match('AbCdefghijk'), 'No')

    def test_edge_case_multiple_mixedcase6(self):
        self.assertEqual(match('AbCdefghijkl'), 'No')

    def test_edge_case_multiple_mixedcase7(self):
        self.assertEqual(match('AbCdefghijklm'), 'No')

    def test_edge_case_multiple_mixedcase8(self):
        self.assertEqual(match('AbCdefghijklmn'), 'No')

    def test_edge_case_multiple_mixedcase9(self):
        self.assertEqual(match('AbCdefghijklmno'), 'No')

    def test_edge_case_multiple_mixedcase10(self):
        self.assertEqual(match('AbCdefghijklmnop'), 'No')

    def test_edge_case_multiple_mixedcase11(self):
        self.assertEqual(match('AbCdefghijklmnopq'), 'No')

    def test_edge_case_multiple_mixedcase12(self):
        self.assertEqual(match('AbCdefghijklmnopqr'), 'No')

    def test_edge_case_multiple_mixedcase13(self):
        self.assertEqual(match('AbCdefghijklmnopqrs'), 'No')

    def test_edge_case_multiple_mixedcase14(self):
        self.assertEqual(match('AbCdefghijklmnopqrst'), 'No')

    def test_edge_case_multiple_mixedcase15(self):
        self.assertEqual(match('AbCdefghijklmnopqrstu'), 'No')

    def test_edge_case_multiple_mixedcase16(self):
        self.assertEqual(match('AbCdefghijklmnopqrstuv'), 'No')

    def test_edge_case_multiple_mixedcase17(self):
        self.assertEqual(match('AbCdefghijklmnopqrstuvw'), 'No')

    def test_edge_case_multiple_mixedcase18(self):
        self.assertEqual(match('AbCdefghijklmnopqrstxyz'), 'No')

    def test_edge_case_multiple_mixedcase19(self):
        self.assertEqual(match('AbCdefghijklmnopqrstuwx'), 'No')

    def test_edge_case_multiple_mixedcase20(self):
        self.assertEqual(match('AbCdefghijklmnopqrstuvwxy'), 'No')
