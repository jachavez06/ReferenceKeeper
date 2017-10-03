#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 19:51:48 2017

@author: jesse
"""

class Reference:
    """Represents a single entry"""
    
    #kind = 'canine'         # class variable shared by all instances

    def __init__(self):
        # instance variables unique to each Reference instance
        self.source_type = 'Journal Article'
        self.article_title = ''
        self.journal_title = ''
        self.volume_number = None
        self.issue_number = None
        self.year_published = None
        self.pages_start = None
        self.pages_end = None
        self.file = None
    
