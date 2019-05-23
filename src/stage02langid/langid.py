'''
Created on 7 Apr 2019

@author: bogdan
'''

import sys, os, re
from collections import defaultdict


class clLangID(object):
    '''
    language identification filtering
    '''


    def __init__(self, FNGramTable, FNoisyCorpus, FOutputCleanKeep, FOutputCleanRemove, FOutputCleanLog):
        '''
        Constructor
        '''
        RENGrams = self.readNGramTable(FNGramTable)
        self.filterCorpus(RENGrams, FNoisyCorpus, FOutputCleanKeep, FOutputCleanRemove, FOutputCleanLog)
        
    
    def readNGramTable(self, FNGramTable):
        iCount = 0
        LNGrams = []
        for SLine in FNGramTable:
            SLine = SLine.rstrip()
            iCount += 1
            if (iCount % 100 == 0): sys.stderr.write(str(iCount) + '. ' + SLine + '\n')
            if SLine.startswith('#'): continue
            try:
                (SNGram, Frq) = re.split('[\t]', SLine, 1)
            except:
                continue
            LNGrams.append(SNGram)
        # SRENGrams = '(' + '|'.join(LNGrams) + ')'
        SRENGrams = '|'.join(LNGrams)
        sys.stderr.write(SRENGrams + '\n')
        # RENGrams = re.compile(SRENGrams, re.IGNORECASE)
        RENGrams = re.compile(SRENGrams)
        return RENGrams
    
    
    def filterCorpus(self, RENGrams, FNoisyCorpus, FOutputCleanKeep, FOutputCleanRemove, FOutputCleanLog):
        '''
        main function for filtering lines that sound Russian
        '''
        iCount = 0
        DProductivity = defaultdict(int)

        for SLine in FNoisyCorpus:
            SLine = SLine.rstrip()
            iCount += 1
            if (iCount % 500000 == 0): sys.stderr.write(str(iCount) + '. ' + SLine + '\n')
            m1 = re.search(RENGrams, SLine)
            if m1:
                # tm1 = type(m1); sys.stderr.write('%(tm1)s' % locals())
                # SMatch = str(m1.group(0))
                # tsline = type(SLine); sys.stderr.write('%(tsline)s' % locals())
                # tsmatch = type(SMatch); sys.stderr.write('%(tsmatch)s' % locals())
                
                # FOutputCleanRemove.write(SLine + '\t' + SMatch + '\n')
                '''
                if (len(m1.group(0)) > 1):
                    
                '''
                FOutputCleanRemove.write(SLine + '\t' + m1.group(0) + '\n')
                DProductivity[m1.group(0)] += 1
                
            else:
                FOutputCleanKeep.write(SLine + '\n')
            
        
        for (SNgram, IFrq) in sorted(DProductivity.items(), key=lambda x: x[1], reverse=True):
            FOutputCleanLog.write('%(SNgram)s\t%(IFrq)d\n' % locals())
        
        
        return
        
        
if __name__ == '__main__':
    SFNGramTable = sys.argv[1]; FNGramTable = open(SFNGramTable, 'rU')
    SFNoisyCorpus = sys.argv[2]; FNoisyCorpus = open(SFNoisyCorpus, 'rU')
    SFOutputClean = sys.argv[3]; FOutputCleanKeep = open(SFOutputClean + '_uk.txt', 'w'); FOutputCleanRemove = open(SFOutputClean + '_ru.txt', 'w')
    FOutputCleanLog = open(SFOutputClean + '_log.txt', 'w')
    
    
    OLangID = clLangID(FNGramTable, FNoisyCorpus, FOutputCleanKeep, FOutputCleanRemove, FOutputCleanLog)

        