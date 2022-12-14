import unittest
from photo_compare import PhotoCompare

class TestPhotoCompare(unittest.TestCase):
    def setUp(self):
        self.pc = PhotoCompare('test_word')

    def test_LevenshteinDistance(self):
        s = 'test'
        t = 'west'
        self.assertEqual(self.pc.LevenshteinDistance(s, t), 1)

    def test_compare(self):
        self.assertIsInstance(self.pc.template, str)
        self.assertEqual(self.pc.template, expected_template)
        self.assertIsInstance(self.pc.levenshtein_distance, int)
        self.assertEqual(self.pc.levenshtein_distance, expected_levenshtein_distance)
        self.assertIsInstance(self.pc.photo_word, str)
        self.assertEqual(self.pc.photo_word, expected_photo_word)

if __name__ == '__main__':
    unittest.main()
