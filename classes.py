# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:45:57 2019

@author: Tim Laeufer

A collection of classes to be used with the story generator.
"""

class NPC:
    def __init__(self, name = None, relations = None):
        self.name = name
        self.relations = relations
        
        
class Relation:
    """A relation between two npcs"""
    def __init__(self):
        pass
    
    