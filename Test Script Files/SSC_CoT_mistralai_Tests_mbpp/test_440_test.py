import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(find_adverb_position("Quick, brown fox jumps over the lazy dog."), (17, 21, "brown"))
        self.assertEqual(find_adverb_position("The lazy cat sat on the mat."), (8, 12, "lazy"))
        self.assertEqual(find_adverb_position("She runs fast."), (4, 8, "fast"))

    def test_edge_cases(self):
        self.assertEqual(find_adverb_position("The lazy dog."), (None, None, None))
        self.assertEqual(find_adverb_position("The dog runs over the lazy bridge."), (15, 19, "lazy"))
        self.assertEqual(find_adverb_position("The lazy dog runs."), (None, None, None))
        self.assertEqual(find_adverb_position("The dog runs, the cat sleeps."), (None, None, None))

    def test_boundary_cases(self):
        self.assertEqual(find_adverb_position("The lazy dog runs, and the cat sleeps."), (23, 27, "lazy"))
        self.assertEqual(find_adverb_position("The lazy dog runs, the cat sleeps, and the horse jumps over the fence."), (23, 27, "lazy"))
        self.assertEqual(find_adverb_position("The lazy dog runs, the cat sleeps, and the horse jumps over the lazy fence."), (23, 27, "lazy"))

    def test_invalid_input(self):
        self.assertEqual(find_adverb_position(123), (None, None, None))
        self.assertEqual(find_adverb_position(""), (None, None, None))
        self.assertEqual(find_adverb_position("The dog runs ly."), (None, None, None))
        self.assertEqual(find_adverb_position("The dog runs ly, the cat sleeps."), (None, None, None))
