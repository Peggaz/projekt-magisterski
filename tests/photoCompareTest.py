import unittest
from photo_compare import PhotoCompare

class TestPhotoCompare(unittest.TestCase):
    def setUp(self):
        self.pc = PhotoCompare('AAAABbBbbbbbaaaAAAAAAABbBbbbbbaaaAAA')

    def test_LevenshteinDistance(self):
        s = 'test'
        t = 'west'
        self.assertEqual(self.pc.LevenshteinDistance(s, t), 1)

    def test_compare(self):
        expected_template = 'AAAABbBbbbbbaaaAAA'
        self.assertIsInstance(self.pc.template, str)
        self.assertEqual(self.pc.template, expected_template)
        self.assertIsInstance(self.pc.levenshtein_distance, int)
        self.assertEqual(self.pc.levenshtein_distance, 0)
        self.assertIsInstance(self.pc.photo_word, str)
        self.assertEqual(self.pc.photo_word, '<mark id='compare_word'>AAAABbBbbbbbaaaAAA</mark>AAAABbBbbbbbaaaAAA')

if __name__ == '__main__':
    unittest.main()
