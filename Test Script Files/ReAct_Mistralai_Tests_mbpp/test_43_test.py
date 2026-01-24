import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_valid_match(self):
        self.assertEqual(text_match('validIdentifier'), 'Found a match!')
        self.assertEqual(text_match('ValidIdentifier'), 'Found a match!')
        self.assertEqual(text_match('valid_identifier'), 'Found a match!')
        self.assertEqual(text_match('Valid_Identifier'), 'Found a match!')

    def test_invalid_match(self):
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match('1validIdentifier'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier1'), 'Not matched!')
        self.assertEqual(text_match('valid_identifier1'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier_'), 'Not matched!')
        self.assertEqual(text_match('_validIdentifier'), 'Not matched!')
        self.assertEqual(text_match('valid_'), 'Not matched!')
        self.assertEqual(text_match('_valid'), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_match('validIdentifier#'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier@'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier$'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier%'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier&'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier*'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier('), 'Not matched!')
        self.assertEqual(text_match('validIdentifier)'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier+'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier-'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier_'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier.'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier,'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier;'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier:'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier="'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier\''), 'Not matched!')
        self.assertEqual(text_match('validIdentifier['), 'Not matched!')
        self.assertEqual(text_match('validIdentifier]'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier{'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier}'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier|'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier^'), 'Not matched!')
        self.assertEqual(text_match('validIdentifier~'), 'Not matched!')
