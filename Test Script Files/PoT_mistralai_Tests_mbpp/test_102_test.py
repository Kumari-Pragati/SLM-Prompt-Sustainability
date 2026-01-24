import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(snake_to_camel('this_is_a_test'), 'thisIsATest')
        self.assertEqual(snake_to_camel('another_test'), 'anotherTest')
        self.assertEqual(snake_to_camel('multi_word_test'), 'multiWordTest')

    def test_edge_and_boundary_cases(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel('single_'), 'Single_')
        self.assertEqual(snake_to_camel('test_'), 'Test_')
        self.assertEqual(snake_to_camel('test_1'), 'Test1')
        self.assertEqual(snake_to_camel('test_123'), 'Test123')
        self.assertEqual(snake_to_camel('test_123_456'), 'Test123456')
        self.assertEqual(snake_to_camel('test_123_456_789'), 'Test123456789')
