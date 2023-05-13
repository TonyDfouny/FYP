import unittest

import sys

sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\Database"))
sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\PhoeEng"))
import PhoeEng.PhoePossessiveFinder

Ph=PhoeEng.PhoePossessiveFinder.PhoePossessiveFinder
class MyTestCase(unittest.TestCase):
    def test_my(self):
        self.assertEqual(Ph('ʾby').Translate(), 'my father')  # add assertion here

    def test_your(self):
        self.assertEqual(Ph('ʾbkm').Translate(), 'your father')  # add assertion here
        self.assertEqual(Ph('ʾbk').Translate(), 'your father')  # add assertion here

    def test_his(self):
        self.assertEqual(Ph('ʾbh').Translate(), 'his father')  # add assertion here

    def test_our(self):
        self.assertEqual(Ph('ʾbn').Translate(), 'our father')  # add assertion here

    def test_their(self):
        self.assertEqual(Ph('ʾbm').Translate(), 'their father')  # add assertion here

if __name__ == '__main__':
    unittest.main()
