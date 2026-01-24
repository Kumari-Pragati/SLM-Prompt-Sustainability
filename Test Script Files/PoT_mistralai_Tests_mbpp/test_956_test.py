import unittest
from ninetyfive sixty_code import split_list

class TestSplitList(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(split_list("ABC DEF GHI"), ["ABC", "DEF", "GHI"])
        self.assertListEqual(split_list("ABC XYZ"), ["ABC"])
        self.assertListEqual(split_list("ABC"), ["ABC"])
        self.assertListEqual(split_list("ABC123"), [])

    def test_edge_case(self):
        self.assertListEqual(split_list("A"), ["A"])
        self.assertListEqual(split_list("AB"), ["AB"])
        self.assertListEqual(split_list("ABC "), ["ABC"])
        self.assertListEqual(split_list("ABC\t"), ["ABC"])
        self.assertListEqual(split_list("ABC\n"), ["ABC"])

    def test_corner_case(self):
        self.assertListEqual(split_list("ABC-123"), ["ABC"])
        self.assertListEqual(split_list("123ABC"), [])
        self.assertListEqual(split_list("ABC_123"), ["ABC"])
        self.assertListEqual(split_list("123_ABC"), [])
