import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello']), 'Matched!')

    def test_typical_case2(self):
        self.assertEqual(check_literals('Hello, world!', ['world']), 'Matched!')

    def test_edge_case(self):
        self.assertEqual(check_literals('Hello, world!', []), 'Not Matched!')

    def test_edge_case2(self):
        self.assertEqual(check_literals('', ['Hello']), 'Not Matched!')

    def test_edge_case3(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world']), 'Matched!')

    def test_edge_case4(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', '']), 'Matched!')

    def test_edge_case5(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world']), 'Matched!')

    def test_edge_case6(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', '']), 'Matched!')

    def test_edge_case7(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world']), 'Matched!')

    def test_edge_case8(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', '']), 'Matched!')

    def test_edge_case9(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world']), 'Matched!')

    def test_edge_case10(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', '']), 'Matched!')

    def test_edge_case11(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', 'world']), 'Matched!')

    def test_edge_case12(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', 'world', '']), 'Matched!')

    def test_edge_case13(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', 'world', 'world']), 'Matched!')

    def test_edge_case14(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', 'world', 'world', '']), 'Matched!')

    def test_edge_case15(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', 'world', 'world', 'world']), 'Matched!')

    def test_edge_case16(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', 'world', 'world', 'world', '']), 'Matched!')

    def test_edge_case17(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', 'world', 'world', 'world', 'world']), 'Matched!')

    def test_edge_case18(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', 'world', 'world', 'world', 'world', '']), 'Matched!')

    def test_edge_case19(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', 'world', 'world', 'world', 'world', 'world']), 'Matched!')

    def test_edge_case20(self):
        self.assertEqual(check_literals('Hello, world!', ['Hello', 'world', 'world', 'world', 'world', 'world', 'world', 'world', 'world', 'world', '']), 'Matched!')
