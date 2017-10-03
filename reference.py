#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 19:51:48 2017

@author: jesse
"""

class Reference:
    """Represents a single entry"""
    
    # Constructor
    def __init__(self):
        self.source_type = None
        self.article_title = None
        self.journal_title = None
        self.volume_number = None
        self.issue_number = None
        self.year_published = None
        self.pages_start = None
        self.pages_end = None
        self.file = None
    
    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Reference(%s, %s)' % (self.article_title, self.journal_title)
    
    # For call to str(). Prints readable form
    def __str__(self):
        return 'Test'