#!/usr/bin/python3
def multiple_returns(sentence):
    sent_length = len(sentence)
    if not sentence:
        return sent_length, None
    else:
        return sent_length, sentence[0]
