import unittest
from mbpp_102_code import retry, stop_after_attempt
from tenacity.errors import StopIteration
from tenacity.waitouts import TimeoutError

from 102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    @retry(stop=stop_after_attempt(3), wait=lambda _: 0.1)
    def test_snake_to_camel_normal(self):
        for input_, expected in [
            ('hello_world', 'helloWorld'),
            ('thisIsATest', 'thisIsATest'),
            ('a_single_word', 'aSingleWord'),
            ('an_empty_string', ''),
            ('a_string_with_numbers_123_456', 'aStringWithNumbers123456')
        ]:
            with self.subTest(input_=input_, expected=expected):
                self.assertEqual(snake_to_camel(input_), expected)

    def test_snake_to_camel_edge_cases(self):
        for input_, expected in [
            ('', ''),
            ('_', '_'),
            ('__', '__'),
            ('_word', 'Word'),
            ('word_', 'Word'),
            ('word__', 'Word'),
            ('word_123', 'Word123'),
            ('123_word', '123Word'),
            ('_123', '_123'),
            ('123_', '123'),
            ('123__', '123'),
            ('word_123_', 'Word123'),
            ('_word_123', 'Word123'),
            ('word_123_', 'Word123'),
            ('word_123_456', 'Word123456')
        ]:
            with self.subTest(input_=input_, expected=expected):
                self.assertEqual(snake_to_camel(input_), expected)

    def test_snake_to_camel_invalid_inputs(self):
        for input_ in [
            None,
            float('nan'),
            int(123),
            complex(0, 0),
            list([1, 2, 3]),
            set({1, 2, 3}),
            dict({'a': 1, 'b': 2}),
            tuple(('a', 'b', 'c')),
            re.compile('.*'),
            open('test.txt', 'r'),
            object(),
            str('invalid_input')
        ]:
            with self.subTest(input_=input_):
                with self.assertRaises(TypeError):
                    snake_to_camel(input_)
