import unittest
from mbpp_254_code import words_ae

class TestWordsAE(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(words_ae('ae hello ae world'), ['hello', 'world'])
        self.assertEqual(words_ae('ae hello ae world ae'), ['hello', 'world', 'ae'])
        self.assertEqual(words_ae('ae hello world ae'), ['hello', 'world'])

    def test_edge_cases(self):
        self.assertEqual(words_ae(''), [])
        self.assertEqual(words_ae('ae'), ['ae'])
        self.assertEqual(words_ae('a'), [])
        self.assertEqual(words_ae('e'), [])

    def test_corner_cases(self):
        self.assertEqual(words_ae('aeaeaeae'), ['aeaeaeae'])
        self.assertEqual(words_ae('aeaeaeaeae'), ['aeaeaeaeae'])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            words_ae(123)
        with self.assertRaises(TypeError):
            words_ae(None)
        with self.assertRaises(TypeError):
            words_ae(True)
