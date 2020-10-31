# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 23:28:31 2020

@author: User
"""
import yaml
import numpy as np
from preprocessor import PreprocessDoc

class Summariser:
    
    def __init__(self):
        with open('../config/config.yml','r') as fl:
            self.config=yaml.load(fl)
        
    def loadDocs(self,filePath):
        with open(filePath,'r') as fl:
            text=fl.read()
        return text    
        
    def splitSentences(self,text):
        sentences=text.split('.')
        return sentences
    
    def groupSentences(self,sentences):
        firstSent,restOfSent=sentences[0],sentences[1:]
        return firstSent,restOfSent
 
    def findSentenceLength(self,text):
        return text.split()
    
    def findSentLengthArray(self, sentences):
        return [self.findSentenceLength(sent) for sent in sentences]
    
    def findTopSentences(self,sentLengths,sentences):
        sortedIdx=np.argsort(sentLengths)
        top3Idx=sortedIdx[-3:]
        top3Sentences=[sentences[i] for i in top3Idx]
        return top3Sentences
    
    def preprocess(self,text):
        preprocessObj = PreprocessDoc()
        #filteredText=preprocessObj.removeSplChar(text)
        filteredText=preprocessObj.convertToLower(text)
        return filteredText
        
    def findSummary(self):
        filePath=self.config['data_path']['train_data']
        text = self.loadDocs(filePath)
        text=self.preprocess(text)
        sentences=self.splitSentences(text)
        firstSent,restOfSent=self.groupSentences(sentences)
        sentLengths=self.findSentLengthArray(restOfSent)
        topSentences=self.findTopSentences(sentLengths,restOfSent)
        allSentences=[firstSent] + topSentences
        summary = ' '.join(allSentences)
        return summary
       
#summariserObj=Summariser()   
#summary=summariserObj.findSummary()