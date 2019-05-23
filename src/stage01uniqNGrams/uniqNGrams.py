#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 5 Apr 2019

@author: bogdan
'''

import sys, os, re
from collections import defaultdict


class clUniqNGrams(object):
    '''
    input: two corpora in two languages
    output: two tables of N-grams sorted by length, shortest to longest: which N-grams are unique and most frequent...
        purpose: for cleaning Ukrainian corpus from Russian segments / texts, etc.
    '''


    def __init__(self, FInput1, FInput2):
        '''
        Constructor
        '''
        sys.stderr.write('init\n')
                
        DNgrams1, DWords1 = self.file2ngramdicts(FInput1)
        DNgrams2, DWords2 = self.file2ngramdicts(FInput2)
        
        # sys.stdout.write('\n')
        self.printDifference(DNgrams1, DNgrams2) # print only uniq for source language
        self.printDictDiff(DWords1, DWords2) # print only uniq for source language

        # self.printDifference(DNgrams2, DNgrams1)
        

        return
    
    def printDifference(self, DNgrams1, DNgrams2):
        LPrinted = []
        for (SNGram, ILen) in sorted (DNgrams1.keys(), key=lambda x: x[1]):
            if (SNGram, ILen) not in DNgrams2.keys():
                Frq = DNgrams1[(SNGram, ILen)]
                if Frq < 3: continue
                if re.match('[А-ЯЄІЇҐЭЁ]', SNGram): continue # no proper names
                BFound = False
                for el in LPrinted:
                    if el in SNGram: BFound = True
                
                if BFound:
                    sys.stderr.write(SNGram + ' - skipped\n')
                else:
                    LPrinted.append(SNGram)
                    FOutputNGrams.write(SNGram + '\t' + str(Frq) + '\n')
                    
        return
        
    
    def printDictDiff(self, DWords1, DWords2):

        for SWord, Frq in sorted (DWords1.items(), key=lambda x: x[1], reverse=True):
            if Frq < 3: continue
            if re.match('[А-ЯЄІЇҐЭЁ]', SWord): continue
            if SWord not in DWords2.keys():
                # Frq = DWords1[SWord]
                FOutputDWords.write(SWord + '\t' + str(Frq) + '\n')
            else:
                FOutputDWJoin.write(SWord + '\t' + str(Frq) + '\n')
   


    
    def file2ngramdicts(self, FInput):
        DNGrams = defaultdict(int)
        DWords = defaultdict(int)
        i = 0
        LINgramSizes = [1, 2, 3]
        for SLine in FInput:
            i+=1; 
            SLine = SLine.rstrip()
            if i % 1000 == 0: sys.stderr.write('string: %(i)d : %(SLine)s \n' % locals())
            
            LWords = re.split('[ \.,\!\:\;\?\-\(\)\[\]0-9\"A-Za-z]+', SLine)
            for SWord in LWords:
                DWords[SWord]+=1
            
            for IPosition in range( len(SLine) ):
            # for IPosition, SCharacter in enumerate():
                for IEl in LINgramSizes: # for each N-gram length
                    try:
                        SNGram = SLine[IPosition : (IPosition + IEl)]
                        if re.search('[ \.,\:\;\?\-\(\)\[\]0-9\"A-Za-z]', SNGram): continue
                        # if not re.match('/^[А-ЯІЇЄҐґ\'а-яіїєґ]+$/', SNGram): continue
                        
                        ILenNGram = len(SNGram)
                        DNGrams[(SNGram, ILenNGram)] += 1

                    except:
                        # sys.stderr.write('index error\n')
                        continue

            
            
            # LNGrams = self.string2ngrams(SLine, [1,2,3,4])
            # for SNGram in LNGrams:
            
        
        
        
        
        return DNGrams, DWords
    
    
if __name__ == '__main__':
    SFInput1 = sys.argv[1]; FInput1 = open(SFInput1, 'rU')
    SFInput2 = sys.argv[2]; FInput2 = open(SFInput2, 'rU')
    
    SFOutputName = sys.argv[3]
    FOutputNGrams = open(SFOutputName + '_ngrams.txt', 'w')
    FOutputDWords = open(SFOutputName + '_dwords.txt', 'w')
    FOutputDWJoin = open(SFOutputName + '_dwjoin.txt', 'w')
    
    OUniqNGrams = clUniqNGrams(FInput1, FInput2)
    
        