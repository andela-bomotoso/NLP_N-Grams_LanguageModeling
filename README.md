# NLP_N-Grams_LanguageModelling
A program that uses n-grams for language modeling and word prediction. This program constructs bigrams and trigrams language models from a training corpus, and use the resulting models to predict words in a test corpus.

### Input
The training and test data input files are gathered from
over 1,700 CNN news stories. Each set contains a single sentence per line. The punctuation, possessives (‘s) and
negations (n’t) have been separated from adjacent text to enable tokenization by using the Python string split
method. Each line in the test file has an integer postfix. This integer is the index (zero based) of the token that
is to be predicted.

### Processing
The processing steps are;
* Each line in the file is considered a sentence. N-grams are extracted at the line/sentence level,
and do not crossover line boundaries. Note: in the unlikely event that some lines contain more than
one sentence, they are handled as a single sentence in this project.
* The data structure used to hold the tokens/words in each sentence are augmented with the
special start sentence ***\<s\>*** and end sentence ***\</s\>*** symbols, as required for each n-gram.
* The extracted unigrams, bigrams, and trigrams are kept in separate data structures (dictionaries
indexed by tuples work well for this).
* Once the n-grams have been extracted, the test file is read for testing. The last element of each
line (an integer) is the index of the token to be predicted. The context is taken from the sentence:

Example sentence: _***My car is painted light <ins>brown</ins>***_ . 5 - Since the (zero based) index for the target word is
5, the word being predicted is brown (shown underlined). The highest probabilities (frequency of
occurrence) bigrams where the first word is light, and trigrams where the first two words are painted
light are assessed.

### Output
The program displays the following output;
* The number of unique unigrams, bigrams, and trigrams extracted
* The number of correct predictions found within the top 1, 3, 5, and 10 bigrams and/or trigrams with the
highest probabilities. The prediction is considered correct when either the bigram or trigram having the
correct conditional context is followed by the word being predicted. 
