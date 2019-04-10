"""
from: http://norvig.com/spell-correct.html
Comments are mine, made in the process of understanding.
"""

from collections import Counter
import re


def words(text):
    """
    Breaks text into words via re.findall(pattern, str) => \w+  pattern to match words
    :param text: str
    :return: List of words from 'text' in lower case
    """
    return re.findall(r'\w+', text.lower())


print("Test words(): ", words("NOW is the time to see what f words() returns and what it doesn't !!!!!!"))

WORDS = Counter(words(open('big.txt').read()))
"""
opens big.txt and reads it, then words() converts text to list of words
Counter is a subclass of dict: key is an object, value is it's counter
WORDS - constant, frequency dictionary based on output of words() on big.txt
"""
print("Test Counter(): ", WORDS)
print("Test Counter(): ", type(WORDS))
print(len(WORDS))
print(sum(WORDS.values()))
print(WORDS.most_common(10))
print('#' * 40)


def P(word, N=sum(WORDS.values())):
    """
    Assert probability of word-argument in WORDS (PEP8: function name should be word_probability)
    :param word: Input arg (a word) from user or function
    :param N: Arg wit default value - sum of values of Counter WORDS, i.e. count of non-unique words in WORDS
    :return: Ratio of word occurrences to count of all words (=probability of word in WORDS)
    """
    return WORDS[word]/N


print("Test P(): ", P("why"))
print('#' * 40)


def correction(word):
    """
    Returns correction of the word-argument based on candidates() and P()
    :param word: Input arg (a word) from user (this is the actual function for user)
    :return: word from candidates-set or -list with maximal probability (key=P)
    """
    return max(candidates(word), key=P)
# print("Test max() evaluation per key: ", max([1, 33], [2, 7, 4], [1], key=len))
# print("Test max() evaluation per key: ", max([1, 33], [2, 7, 4], [1], key=sum))
# # key - specifies which function should be used to evaluate max(): len(), sum() etc.


def candidates(word):
    """
    Generates possible spelling corrections for word based on other functions
    :param word: Any one-word str from correction()
    :return: Word as 1-element list via known(), else set of words with 1 edit, or 2 edits,
    or word as list even if not known
    """
    return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]
# 'or' operator in return statement makes Python return first of these alternatives that is True (returns sth)
# so if word() determines that word 'xxx' is present in our WORDS dictionary, than it returns 'xxx'
# otherwise it evaluates known(edits1(word)) and so forth
# TODO why square brackets around [word]? hypothesis: convert single word to list to make it digestible for known()
# changing [ ] to { } which is set, seems to have no effect


def known(words):
    """
    Returns list of unique words present (hence 'known') in the text used as database
    :param words: words() function that returns text broken into words
    :return: Dict subset of unique words that appear in dict WORDS
    """
    return set(w for w in words if w in WORDS)
# return statement contains "List comprehension" - way to construct a list


def edits1(word):
    """
    Prepares set of all possible mutations of a word that are one sign away from the input
    :param word: Any one-word str from candidates()
    :return: Set of deletes, transposes, replaces, and inserts
    """
    letters     = 'abcdefghijklmnopqrstuvwxyz'
    splits      = [(word[:i], word[i:]) for i in range(len(word) + 1)]              # possible splits of a word
    deletes     = [L + R[1:]            for L, R in splits if R]                    # possible sums of 2 splits
    transposes  = [L + R[1]+R[0]+R[2:]  for L, R in splits if len(R) > 1]           # possible transposes of 2 letters
    replaces    = [L + c + R[1:]        for L, R in splits if R for c in letters]   # possible 1-letter replaces
    inserts     = [L + c + R            for L, R in splits for c in letters]        # possible 1-letter inserts
    # print('Test splits within edits1():', splits[:10])
    # print('Test deletes within edits1():', deletes[:10])
    # print('Test transposes within edits1():', transposes[:10])
    # print('Test replaces within edits1():', replaces[:10])
    # print('Test inserts within edits1():', inserts[:10])
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


print("Ex. edits1()", edits1('spelink'))
print("Ex. candidates():", candidates("spelink"))
print("Ex. correction():", correction("spelink"))



