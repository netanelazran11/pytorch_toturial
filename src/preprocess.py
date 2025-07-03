def load_corpus():
    corpus = [
        "We always come to Paris",
        "The professor is from Australia",
        "I live in Stanford",
        "He comes from Taiwan",
        "The capital of Turkey is Ankara"
    ]
    return corpus

def load_corpus():
    return ["Example sentence"]

def create_word_windows(corpus, window_size=1):
    """
    יוצר חלונות מילים בגודל נתון ומחזיר (קונטקסט, מילה מרכזית)
    """
    result = []
    for sentence in corpus:
        words = sentence.split()
        for i in range(window_size, len(words) - window_size):
            context = words[i - window_size:i] + words[i + 1:i + window_size + 1]
            target = words[i]
            result.append((" ".join(context), target))
        return result