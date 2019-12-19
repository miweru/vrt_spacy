import unittest
from pathlib import Path

from vrt import Corpus

from vrt_spacy import Annotate


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with Corpus("~", "meinkorpus", 4, "text_name") as c:
            annotate = Annotate(c)
            annotate("Das hier ist mein Text", text_name="Text1")
            annotate("Das hier ist ein weiterer, ziemlich langer Text! ;) " * 30, text_name="Text2")

        mypath = Path("~/meinkorpus.vrt.gz").expanduser().resolve()
        self.assertTrue(mypath.exists())
        text = [line.strip() for line in open(mypath)]
        self.assertIn("<", text[0])
        self.assertIn("<", text[-1])
        self.assertGreater(len(text), 200)


if __name__ == '__main__':
    unittest.main()
