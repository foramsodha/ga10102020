# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 23:27:02 2020

@author: User
"""

import re

class PreprocessDoc:
    
    """
    Module for preprocessing articles
    """
    
    def removeSplChar(text):
        """
        Remove special characters
        
        Input:
            text:string
        Output:
            modifiedText:string
        """
        filteredText=re.sub(',|;|#|$','',text)
        return filteredText
        
    def convertToLower(self,text):
        return text.lower()
        