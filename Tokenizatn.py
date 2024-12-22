
import nltk

from nltk.tokenize import word_tokenize

quote = "All power is within you .You can do anything"

quote_tokens = word_tokenize(quote)
print(quote_tokens)

print(len(quote_tokens))

from nltk.util import bigrams, trigrams, ngrams
string = "One of the steps to be perform in the NLP.It convert unstructured textual text into a proper formal of data"

tokens = word_tokenize(string)
string_bigrams = list(nltk.bigrams(tokens))
print("******************Bigrams******************")
print(string_bigrams)

string_trigrams = list(nltk.trigrams(tokens))
print("******************Trigrams******************")
print(string_trigrams)

string_ngrams = list(nltk.ngrams(tokens, 5))
print("******************Ngrams******************")
print(string_ngrams)