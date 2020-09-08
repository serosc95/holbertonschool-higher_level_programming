#!/usr/bin/python3
def multiple_returns(sentence):
    letter = None
    if sentence:
        letter = sentence[:1]
    result = (len(sentence), letter)
    return (result)
