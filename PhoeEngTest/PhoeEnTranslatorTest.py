import unittest
import sys

sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\Database"))
sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\PhoeEng"))
import PhoeEng.PhoeEnTranslator

Ph=PhoeEng.PhoeEnTranslator.PhoeEnTranslate
class MyTestCase(unittest.TestCase):
    """
    Testing only the call of functions with easy tests
    """
    def test_onecomonwords(self):
        self.assertEqual(Ph('ḥlt'),' coffin')  # add assertion here

    def test_oneverb(self):
        self.assertEqual(Ph('ʾpʿl'), ' *make')  # add assertion here
    def test_onepossessive(self):
        self.assertEqual(Ph('ʾbh'), ' his father')  # add assertion here
    def test_oneAlword(self):
        self.assertEqual(Ph('wʾb'), ' and father')  # add assertion here

if __name__ == '__main__':
    unittest.main()
