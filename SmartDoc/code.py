# Copyright (C) 2019 Hui Lan
# The following line fixes SyntaxError: Non-UTF-8 code starting with ...
# coding=utf8

import string
#{see rq1}
def remove_punctuation(s):
    p = ',.:’“”' + string.punctuation
    t = ''
    for c in s:
        if not c in p:
            t += c
        elif c == '’': # handle the case such as May’s
            return t
    return t
#{see rq2}
def file2lst(fname):
    ''' Return a list where each element is a word from fname. '''
    L = []
    f = open(fname)
    for line in f:
        line = line.strip()
        lst = line.split()
        for x in lst:
            L.append(x)
    f.close()
    return L
#{see rq3}
def lst2dict(lst):
    ''' Return a dictionary given list lst.  Each key is an element in the lst.
    The value is always 1.'''
    d = {}
    for w in lst:
        d[w] = 1 
    return d

#{see rq4}
class WordFreq:
    
    def __init__(self, filename, english_dictionary):
        self.ed = english_dictionary
        self.fname = filename
        self.freq_lst = None
    
    
    def get_word_frequency(self):
        ''' 
        Assign the attribute freq_lst with a list of tuples, in the following form:
        [('the', 55), ('and', 19), ('to', 19), ('of', 16), ('on', 15), ('may', 13), ('deal', 13)]
        '''
        self.freq_lst = [] # modify this such that it becomes something like  [('the', 55), ('and', 19), ('to', 19), ('of', 16)]

    
    def __str__(self):
        s = ''
        # Insert your code here
        return s
    

if __name__ == '__main__':    
    ed = lst2dict(file2lst('words.txt')) # from http://greenteapress.com/thinkpython2/code/words.txt
    wf = WordFreq('brexit-news.txt', ed)
    print(wf) # this statement will print something as follows.
    #the (55)
    #and (19)
    #to (19)
    #of (16)
    #on (15)
    #may (13)
    #deal (13)