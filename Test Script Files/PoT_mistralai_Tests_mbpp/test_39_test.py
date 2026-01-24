import unittest
from mbpp_39_code import rearange_string

class TestRearrangeString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(rearrange_string(""), "")

    def test_single_character(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(rearrange_string(char), char)

    def test_two_characters(self):
        for char1 in "abcdefghijklmnopqrstuvwxyz":
            for char2 in "abcdefghijklmnopqrstuvwxyz":
                if char1 > char2:
                    self.assertEqual(rearrange_string(char1 + char2), char2 + char1)

    def test_multiple_characters(self):
        test_cases = [
            ("aaabbbccc", "abcabcabc"),
            ("aaabbbcccdd", "abcbcabcdd"),
            ("aaabbbcccddde", "abcbcabcddde"),
            ("aaabbbcccdddeee", "abcbcabcdddeee"),
            ("aaabbbcccdddeeeff", "abcbcabcdddeeeff"),
            ("aaabbbcccdddeeefffgg", "abcbcabcdddeeefffgg"),
            ("aaabbbcccdddeeefffggggg", "abcbcabcdddeeefffggggg"),
        ]
        for test_case in test_cases:
            self.assertEqual(rearrange_string(test_case[0]), test_case[1])

    def test_edge_cases(self):
        self.assertEqual(rearrange_string("a"), "a")
        self.assertEqual(rearrange_string("aa"), "aa")
        self.assertEqual(rearrange_string("aaa"), "aaa")
        self.assertEqual(rearrange_string("aaaa"), "aaaa")
        self.assertEqual(rearrange_string("aaaaa"), "aaaaa")
        self.assertEqual(rearrange_string("aaaaaa"), "aaaaaa")
        self.assertEqual(rearrange_string("aaaaaaa"), "aaaaaaa")
        self.assertEqual(rearrange_string("aaaaaaab"), "aaabaaaa")
        self.assertEqual(rearrange_string("aaaaaaac"), "aaacaaaa")
        self.assertEqual(rearrange_string("aaaaaaad"), "aaadaaaa")
        self.assertEqual(rearrange_string("aaaaaaae"), "aaaeaaaa")
        self.assertEqual(rearrange_string("aaaaaaaf"), "aaafaaaa")
        self.assertEqual(rearrange_string("aaaaaaag"), "aaagaaaa")
        self.assertEqual(rearrange_string("aaaaaaah"), "aaahaaaa")
        self.assertEqual(rearrange_string("aaaaaaai"), "aaaiaaaa")
        self.assertEqual(rearrange_string("aaaaaaaj"), "aaajaaaa")
        self.assertEqual(rearrange_string("aaaaaaak"), "aaakaaaa")
        self.assertEqual(rearrange_string("aaaaaaal"), "aaalaaaa")
        self.assertEqual(rearrange_string("aaaaaaam"), "aaamaaaa")
        self.assertEqual(rearrange_string("aaaaaaan"), "aaanaaaa")
        self.assertEqual(rearrange_string("aaaaaaao"), "aaaoaaaa")
        self.assertEqual(rearrange_string("aaaaaaap"), "aaapaaaa")
        self.assertEqual(rearrange_string("aaaaaaaq"), "aaaqaaaa")
        self.assertEqual(rearrange_string("aaaaaaar"), "aaaraaaa")
        self.assertEqual(rearrange_string("aaaaaaas"), "aaasaaaa")
        self.assertEqual(rearrange_string("aaaaaaat"), "aaataaaa")
        self.assertEqual(rearrange_string("aaaaaaau"), "aaauaaaa")
        self.assertEqual(rearrange_string("aaaaaaav"), "aaavaaaa")
        self.assertEqual(rearrange_string("aaaaaaaw"), "aaawaaaa")
        self.assertEqual(rearrange_string("aaaaaa