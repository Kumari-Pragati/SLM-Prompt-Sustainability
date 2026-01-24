import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_find_adverb_position(self):
        self.assertEqual(find_adverb_position("Hello world"), None)
        self.assertEqual(find_adverb_position("Hello worldly"), None)
        self.assertEqual(find_adverb_position("Hello worldly again"), None)
        self.assertEqual(find_adverb_position("Hello worldly again today"), None)
        self.assertEqual(find_adverb_position("Hello worldly again today happily"), (24, 31, "happily"))
        self.assertEqual(find_adverb_position("Hello worldly again today happily tomorrow"), (24, 31, "happily"))
        self.assertEqual(find_adverb_position("Hello worldly again today happily tomorrow again"), (24, 31, "happily"))
        self.assertEqual(find_adverb_position("Hello worldly again today happily tomorrow again happily"), (24, 31, "happily"))
        self.assertEqual(find_adverb_position("Hello worldly again today happily tomorrow again happily today"), (24, 31, "happily"))
        self.assertEqual(find_adverb_position("Hello worldly again today happily tomorrow again happily today again"), (24, 31, "happily"))
