#   Bukola Grace Omotoso
#   CSCI 6350-001
#   Project #2
#   Due: 02/08/20

# Language Modelling with N-GRAMS


'''WHY I BELIEVE THE RESULT ARE CORRECT
    Shuffling the lines in train_txt and test_txt files
    gives the same result. Also, it is logical to have more
    results as the N increases in the top N ranking analysis
    
    PROS TO HAVING THE SENTENCE IN EITHER OF THE TEST OR TRAINING FILE
    The randomness of our analysis is guaranted and thereby providing a reliable
    result.
    
    CONS TO HAVING THE SENTENCE IN EITHER OF THE TEST OR TRAINING FILE
    Due to the selection being random, in a rare case, we may end up
    having the all the test sentence coming only form the train data or
    test data. In that case, we will not be able to make any meaning from
    our analysis.
    
    Also, in real life, we do not stick to just the test set, language evolve,
    that is why our training needs to be more robust in order for it to correctly 
    depict a real life model usage.
    

    A BETTER WAY TO SPLIT THE DATA INTO TRAINING AND TEST COMPONENTS
    - In the sentences, there are instances where a bigram or trigram cannot
      be generated, e.g if index the index in a sentence is 0 as we have in
      line 71 of the test data, we cannot test for correctnes as there is no bigram 
      or trigram to compare. Ensuring that indexes are not lower than 2 will guarantee  that
      we always have a basis for our comparison since we can always find the prefix bigrams 
      and trigrams
      
    - A better way will be to classify the training data based on some parameters
      and ensure all the classes are well represented in the test data. Ensuring
      all classes of the data are all represented will guarantee the completeness
      of the analysis. In summary, creating a more robust training set such that regardless
      of our test data not in train data, we will still have a working model


'''

    

import string
import csv
import random
import re
from collections import Counter 

test_bigrams = []
test_trigrams = []

#import the training data
def importTrainingSet(  ):
    infile = open('train.txt', 'r')
    train_set = infile.read().splitlines()
    return train_set

#import the test data
def importTestSet():
    test_set = []
    infile = open('test.txt', 'r')
    for line in infile:
        test_set.append(line)
    return test_set
    

# Count unique ngrams and pass into a dictionary
def generateNgrams(train, n, ngramsdict):
    train_set = []
    cnt = 0
    for item in train:
        if item.strip():
            line = formatNgrams(item, n)
            for word in line.split():
                train_set.append(word)
    ngrams = zip(*[train_set[i:] for i in range(n)])
    retngrams =  [" ".join(ngram) for ngram in ngrams]
    
    for word in retngrams:
        # Check if the word is already in dictionary 
        if word in ngramsdict: 
            # Increment count of word by 1 
            ngramsdict[word] = ngramsdict[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            ngramsdict[word] = 1
            cnt+=1
    return cnt;


#format ngrams
def formatNgrams(line,n):
    pad1 = ""
    pad2 = ""
    if (n == 1 or n == 2):
        pad1 ="<s> "
        pad2 = " </s>"
        return pad1+line+pad2;

    if (n == 3):
        pad1 ="<s><s> "
        pad2 = " </s></s>"
        return pad1+line+pad2;


# Given a dictionary, find the top N count of an item in the dictionary
def findTopN(bigrams_dict, trigrams_dict, N, key):
    cnt = 0
    b_topN = dict()
    t_topN = dict()
    found = False
    if (len(bigrams_dict) > 0):
         k = Counter(bigrams_dict)
         b_topN = k.most_common(N)
         
    if (len(trigrams_dict) > 0):
         k = Counter(trigrams_dict)
         t_topN = k.most_common(N)
        
    for itm in b_topN:
            if itm[0].split()[1] == key:
                found = True
                cnt+=1
                break
                
    # if the word is not found within bigrams, check within trigrams
    if(found == False):
        for itm in t_topN:
            if itm[0].split()[2] == key:
                cnt+=1
                break
    return cnt;

def generateLog(counts, total_predic):
    N = [1, 3, 5, 10]
    i = 0
    for cnt in counts:
        print("# of times correct word found in top ", N[i]," highest probability n-grams ",cnt," of ",total_predic);
        i+=1
    

def main():
    test_set = importTestSet()
    train_set = importTrainingSet()
    unigrams = dict()
    bigrams = dict()
    trigrams = dict()
    
    print("Unique unigrams extracted: ",generateNgrams(train_set, 1, unigrams));
    print("Unique bigrams extracted: ", generateNgrams(train_set, 2, bigrams));
    print("Unique trigrams extracted: ", generateNgrams(train_set, 3, trigrams));

    # Declare variable to hold the counts
    cnt1 = 0
    cnt3 = 0
    cnt5 = 0
    cnt10 = 0
    ln=0
    
    # Loop through the line in the test data and analyze
    for line in test_set:
        found = False
        bigrams_dict = dict()
        trigrams_dict = dict()
        ln+=1
        words = line.split(" ")
        key_idx = words[-1]
        idx = int(key_idx)
        key = words[idx]
        
        #Fetch all bigrams that match the prefix
        if (idx > 0):
            prefix = words[idx-1]
            for bigram in bigrams:
                bgram = bigram.split()[0]
                #Add bigrams that match prefix to dictionary
                if bgram == prefix:
                    #print(bgram, prefix);
                    bigrams_dict[bigram] = bigrams[bigram];
       
        #Fetch all trigrams that match the prefix
      
        if (idx > 1):
        # Process trigrams
            prefix = words[idx-2]+" "+words[idx-1]

            #Fetch all trigrams that match the prefixes
            for trigram in trigrams:
                tgram = trigram.split()[0]+" "+trigram.split()[1]
                #Add bigrams that match prefix to dictionary
                if tgram == prefix:
                    trigrams_dict[trigram] = trigrams[trigram]
                    
        # Sort the dictionary for top N values
        cnt1  += findTopN(bigrams_dict, trigrams_dict, 1, key)
        cnt3  += findTopN(bigrams_dict, trigrams_dict, 3, key)
        cnt5  += findTopN(bigrams_dict, trigrams_dict, 5, key)
        cnt10 += findTopN(bigrams_dict, trigrams_dict, 10,key)
        
    counts = [cnt1, cnt3, cnt5, cnt10]
    generateLog(counts, ln)
    

        


        
    

main();
