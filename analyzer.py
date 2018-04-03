import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positivewords = set()
        self.negativewords = set()
        
        fileP = open(positives,'r')
        for line in fileP:
            if line.startswith(';'):
                pass
            else:
                self.positivewords.add(line.strip(' \t\n\r'))
        
        fileN = open(negatives, 'r')
        for line in fileN:
            if line.startswith(';'):
                pass
            else:
                self.negativewords.add(line.strip(' \t\n\r'))
        
        # TODO

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        
        score = 0
        tokenizer = nltk.tokenize.TweetTokenizer()  
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            token = str.lower(token)
            if token in self.positivewords:
                score += 1
            elif token in self.negativewords:
                score -= 1
            else:
                pass
        return score