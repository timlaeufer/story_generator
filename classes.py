# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:45:57 2019

@author: Tim Laeufer

A collection of classes to be used with the story generator.

TODO:
    Inner Circle of people,
    Outer Circle of people,
    
    Trait generation:
        excluding traits
    
    City Generation:
        Name generator
        size
        population
        complexity
        council (council size = pop/15, >3):
            list, maybe dict with list as val, position as key
        Organisation:
            amount_of_organisations = pop % 60 [?]
            with certain chance maybe secret organisations
        jobs:
            [dictionary with lists as values, jobs as keys]
            baker, trader, butcher, farmer, mayor
    
    Opponent generation
    
    Location generation:
        Name generator
    
    Family generation:
        Name generator
"""

class NPC:
    amount_of_npc = 0
    def __init__(self, name = None, relations = None):
        if(name):
            self.name = name
        else:
            self.name = 'NPC ' + str(self.amount_of_npc)
            self.amount_of_npc += 1
        self.relations = relations
        
class City:
    amount_of_cities = 0
    def __init__(self, name = None):
        if(name):
            self.name = name
        else:
            self.name = 'city ' + str(self.amount_of_cities)
            self.amount_of_cities += 1
            
