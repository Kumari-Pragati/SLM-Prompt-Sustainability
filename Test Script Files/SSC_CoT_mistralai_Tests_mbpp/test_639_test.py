import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sample_nam(['John', 'Sara', 'Mike', 'Emma']), 3)

    def test_edge_cases(self):
        self.assertEqual(sample_nam(['jOhn', 'SaRa', 'mIke', 'EmMa']), 3)
        self.assertEqual(sample_nam(['John1', 'Sara#', 'Mike@', 'Emma%']), 0)
        self.assertEqual(sample_nam(['John_', 'Sara-', 'Mike+', 'Emma^']), 0)
        self.assertEqual(sample_nam(['John.', 'Sara,', 'Mike;', 'Emma:']), 0)
        self.assertEqual(sample_nam(['John!', 'Sara?', 'Mike()', 'Emma[]']), 0)
        self.assertEqual(sample_nam(['John\t', 'Sara\n', 'Mike\r', 'Emma\f']), 0)
        self.assertEqual(sample_nam(['John\u0304', 'Sara\u0303', 'Mike\u0302', 'Emma\u0301']), 0)
        self.assertEqual(sample_nam(['John\u200B', 'Sara\u200C', 'Mike\u200D', 'Emma\u200E']), 0)

    def test_empty_input(self):
        self.assertEqual(sample_nam([]), 0)

    def test_single_input(self):
        self.assertEqual(sample_nam(['']), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, sample_nam, 123)
        self.assertRaises(TypeError, sample_nam, ('John',))
        self.assertRaises(TypeError, sample_nam, [1, 2, 3])
