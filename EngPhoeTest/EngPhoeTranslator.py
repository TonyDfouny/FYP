import unittest
import sys

sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\Database"))
sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\EngPhoe"))
import EngPhoe.EngPhoeTranslator

En=EngPhoe.EngPhoeTranslator.EngPhoeTranslator

class MyTestCase(unittest.TestCase):
    def test_onecomonwords(self):
        self.assertEqual(En('Father').Translate(), ' ʾb')  # add assertion here

    def test_oneverb(self):
        self.assertEqual(En('Collect').Translate(), ' ʾry')  # add assertion here
    def test_onepossessive(self):
        self.assertEqual(En('His father').Translate(), ' ʾbh') # add assertion here
    def test_oneAlword(self):
        self.assertEqual(En('The father').Translate(), ' hʾb')  # add assertion here

if __name__ == '__main__':
    unittest.main()
