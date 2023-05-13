import unittest

import sys

sys.path.append(sys.path[1]+r"\EngArPhoe")
sys.path.append(sys.path[1]+r"\Database")
sys.path.append(sys.path[1]+r"\EngPhoe")
import EngArPhoe.ArPhoeTranslator

Ar=EngArPhoe.ArPhoeTranslator.ArPhoeTranslator

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Ar('Father','Offline'), ' ʾb')  # add assertion here


if __name__ == '__main__':
    unittest.main()
