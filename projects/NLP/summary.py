import spacy
from heapq import nlargest


def get_summary(n_ideas, opinions):
    """
    Get the most n important ideas from a set of opinions
    Args:
        n_ideas: desired number of most important ideas
        opinions: dict format opinions in way:  {"opinions":[{"id":<op_id>, "text":<op_text>},...]}

    Returns: The n most important ideas in a single string

    """
    # load corpus
    nlp = spacy.load('en_core_web_lg')

    full_text = ""
    for curr_op in opinions["opinions"]:
        full_text += curr_op["text"] + "."

    doc = nlp(full_text)
    word_freq = {}
    for word in doc:
        # using simple word representation ignoring stop words and punctuation
        word_text = word.text.lower()
        if word_text not in nlp.Defaults.stop_words and word.pos_ != 'PUNCT':
            if word_text not in word_freq:
                word_freq[word_text] = 1
            else:
                word_freq[word_text] += 1

    # normalize frecuency vector
    max_freq = max(word_freq.values())
    for word in word_freq:
        word_freq[word] = (word_freq[word] / max_freq)

    # rank by sentence
    sentence_list = [sentence for sentence in doc.sents]
    sent_score = {}
    for sentence in sentence_list:
        # the sentences weight is defined by the frequency of contained words
        for word in sentence:
            if word.text.lower() in word_freq:
                if sentence not in sent_score:
                    sent_score[sentence] = word_freq[word.text.lower()]
                else:
                    sent_score[sentence] += word_freq[word.text.lower()]

    summarized_sent = nlargest(n_ideas, sent_score, key=sent_score.get)
    summary_list = [w.text for w in summarized_sent]
    summary = '.'.join(summary_list)
    return summary
