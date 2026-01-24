import unittest
from mbpp_73_code import multiple_split

class TestMultipleSplit(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(multiple_split('Hello; World, this is a test;'), ['Hello','World, this is a test', ''])

    def test_edge_case(self):
        self.assertEqual(multiple_split('Hello;'), ['Hello', ''])

    def test_edge_case2(self):
        self.assertEqual(multiple_split('Hello; World'), ['Hello','World'])

    def test_edge_case3(self):
        self.assertEqual(multiple_split('Hello'), ['Hello'])

    def test_edge_case4(self):
        self.assertEqual(multiple_split('Hello\nWorld'), ['Hello', 'World'])

    def test_edge_case5(self):
        self.assertEqual(multiple_split('Hello*World'), ['Hello*World'])

    def test_edge_case6(self):
        self.assertEqual(multiple_split('Hello, World'), ['Hello, World'])

    def test_edge_case7(self):
        self.assertEqual(multiple_split('Hello; World, this is a test'), ['Hello','World, this is a test'])

    def test_edge_case8(self):
        self.assertEqual(multiple_split('Hello; World\nthis is a test'), ['Hello','World', 'this is a test'])

    def test_edge_case9(self):
        self.assertEqual(multiple_split('Hello; World* this is a test'), ['Hello','World* this is a test'])

    def test_edge_case10(self):
        self.assertEqual(multiple_split('Hello, World* this is a test'), ['Hello, World* this is a test'])

    def test_invalid_input(self):
        with self.assertRaises(re.error):
            multiple_split('Hello World')
