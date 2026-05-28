from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        self.assertEqual( "SENT_POSITIVE",sentiment_analyzer("I love working with Python")["label" ])
        self.assertEqual( "SENT_NEGATIVE",sentiment_analyzer("I hate working with Python")["label" ])
        self.assertEqual( "SENT_NEUTRAL",sentiment_analyzer("I am neutral on Python")["label" ])


if __name__=="__main__":
    unittest.main()    