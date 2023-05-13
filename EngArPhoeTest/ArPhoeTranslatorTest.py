import unittest

import sys

sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\Database"))
sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\EngArPhoe"))
sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\EngPhoe"))
import EngArPhoe.ArPhoeTranslator

Ar=EngArPhoe.ArPhoeTranslator.ArPhoeTranslator

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Ar('Father','Offline'), ' ʾb')  # add assertion here


if __name__ == '__main__':
    unittest.main()
